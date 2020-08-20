from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Cart

def showcart(request):
    current_customer = request.user.customer
    current_cart = Cart.objects.get(customer_id=current_customer, status="u")
    
    return render(request, 'cart/showcart.html', {'current_cart':current_cart})
