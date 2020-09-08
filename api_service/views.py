# from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsOwner

from content.models import Product, SubCategory, Brand, Attribute, Feedback, ProductAttr
from accounts.models import Customer, Supplier
from Supplier.models import ProductSupplier
from customer.models import CustomerAddress
from cart.models import Cart, OrderItem
from .serializers import (ProductSerializer, CatSerializer, BrandSerializer,
        AttributeSerializer, FeedbackSerializer, ProductAttrSerializer, CustomerSerializer,
        CustomerAddressSerializer, SupplierSerializer, ProductSupplierSerializer,
         CartSerializer, OrderItemSerializer)


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CatView(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = CatSerializer


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class AttributeView(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer


class FeedbackView(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class ProductAttrView(viewsets.ModelViewSet):
    queryset = ProductAttr.objects.all()
    serializer_class = ProductAttrSerializer

class CustomerAddressView(viewsets.ModelViewSet):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerAddressSerializer

class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class SupplierView(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ProductSupplierView(viewsets.ModelViewSet):
    queryset = ProductSupplier.objects.all()
    serializer_class = ProductSupplierSerializer

class CartView(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Cart.objects.all()
        else:
            return Cart.objects.filter(customer_id = self.request.user.customer)

    def update(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = request.user
            prosup_id = serializer.validated_data.get("product_supplier_id")
            # number = serializer.validated_data.get("number")
            try:
                prosup = ProductSupplier.objects.get(id = prosup_id)
            except Exception as e:
                return Response(str(e))
            if not prosup.stock >= 1:
                return Response(f"we do not have enough {prosup}")
            else:
                try:
                    cart = Cart.objects.get(customer_id = user.customer, status='u')
                except:
                    cart = Cart.objects.create(customer_id = user.customer, status='u')
                try:

                    if prosup in cart.order.all().values_list('product_supplier_id', flat=True):
                        # OrderItem.objects.get(cart=cart, product_supplier_id=prosup)
                        return Response(f"{prosup} is already in your cart")
                except:
                    OrderItem.objects.create(cart=cart, product_supplier_id=prosup)
                    return Response(f"{prosup} added to your cart succesfully")


class OrderItemView(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer