# from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsCartOwner, IsOrderOwner

from content.models import Product, SubCategory, Brand, Attribute, Feedback, ProductAttr
from accounts.models import Customer, Supplier
from Supplier.models import ProductSupplier
from customer.models import CustomerAddress
from cart.models import Cart, OrderItem
from .serializers import (ProductSerializer, CatSerializer, BrandSerializer,
        AttributeSerializer, FeedbackSerializer, ProductAttrSerializer, CustomerSerializer,
        CustomerAddressSerializer, SupplierSerializer, ProductSupplierSerializer,
         CartSerializer, OrderItemSerializer, AddToCartSerializer)


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

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        # self.perform_update(serializer)
        addresses = serializer.validated_data.get("address")
        for address in addresses:
            CustomerAddress.objects.create(customer_id=self.request.user.customer)
        
        return Response("پروفایل آپدیت شد")

class SupplierView(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ProductSupplierView(viewsets.ModelViewSet):
    queryset = ProductSupplier.objects.all()
    serializer_class = ProductSupplierSerializer

class CartView(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsCartOwner]
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



class OrderItemView(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOrderOwner]
    # queryset = OrderItem.objects.all()
    # serializer_class = OrderItemSerializer
    

    def get_serializer_class(self):
        if self.action == 'create':
            return AddToCartSerializer
        else:
            return OrderItemSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return OrderItem.objects.all()
        else:
            # print('-------------------')
            return OrderItem.objects.filter(cart_id__customer_id = self.request.user.customer)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        # if serializer.is_valid(raise_exception=True):
        serializer.is_valid(raise_exception=True)
        user = request.user
        prosup = serializer.validated_data.get("product_supplier_id")
        if not prosup.stock >= 1:
            return Response("we do not have any ")
        else:
            try:
                cart = Cart.objects.get(customer_id = user.customer, status='u')
            except:
                cart = Cart.objects.create(customer_id = user.customer, status='u')
            
            if prosup.id in cart.order.all().values_list('product_supplier_id', flat=True):
                return Response(" is already in your cart")
            else:
                OrderItem.objects.create(cart_id=cart, product_supplier_id=prosup)
                return Response(" added to your cart succesfully")

# class OrderItemView(viewsets.ModelViewSet):
#     queryset = OrderItem.objects.all()
#     serializer_class = OrderItemSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated, IsOrderOwner]