from django.shortcuts import render 
from .models import *
# Create your views here.
def show_all_suppliers(request):
    return render(request, 'Supplier/supplier.html')

def show_supplier(request):
    pass