from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , logout

# Create your views here.
def show_all_suppliers(request):
    return render(request, 'Supplier/supplier.html')

def show_supplier(request):
    pass

def logout(request):
    logout(request)
    return redirect('content')
