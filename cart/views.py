from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def showcart(request):
    current_user = request.user
    current_cart = Cart.objects.get(customer_id=current_user, status=u)
    
    return render(request, 'cart/showcart.html', {})
