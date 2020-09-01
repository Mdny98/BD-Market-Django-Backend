# from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from content.models import Product, SubCategory, Brand
from .serializers import ProductSerializer, CatSerializer, BrandSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CatView(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = CatSerializer


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

