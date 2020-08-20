from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Cart


def showcart(request):
    if request.method == 'GET':
        current_customer = request.user.customer
        current_cart = Cart.objects.get(customer_id=current_customer, status="u")
        
        return render(request, 'cart/showcart.html', {'current_cart':current_cart})

    if request.method == 'POST':
        current_customer = request.user.customer
        prosup = request.POST.get('prosup')
        current_cart, created = Cart.objects.get_or_create(
                                    customer_id=current_customer,
                                    status='u',)
        OrderItem(cart_id=current_cart, product_supplier_id=prosup, number=1)
        return render(request, 'cart/showcart.html')