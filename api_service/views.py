# from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from content.models import Product, SubCategory, Brand, Attribute, Feedback, ProductAttr
from accounts.models import Customer
from .serializers import (ProductSerializer, CatSerializer, BrandSerializer,
        AttributeSerializer, FeedbackSerializer, ProductAttrSerializer, CustomerSerializer)


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

class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer