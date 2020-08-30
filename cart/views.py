from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import F

from .models import Cart, OrderItem
from Supplier.models import ProductSupplier
# Create your views here.

from .models import Cart


def showcart(request):
    if request.method == 'GET':
        current_customer = request.user.customer
        try:
            current_cart = Cart.objects.get(customer_id=current_customer, status="u")
            # current_cart = get_object_or_404(Cart, customer_id=current_customer, status="u")
            return render(request, 'cart/showcart.html', {'current_cart':current_cart})
        except:
            return render(request, 'cart/showcart.html')
            # 'error': 'Bad info!'


    if request.method == 'POST':
        current_customer = request.user.customer
        prosupid = request.POST.get('prosupid')
        # print(f'\nprosup_id is{prosup_id}')
        prosup = ProductSupplier.objects.get(pk=prosupid)
        current_cart, created = Cart.objects.get_or_create(
                                    customer_id=current_customer,
                                    status='u',)
        quantity = request.POST.get('quantity')
        order_item, created = OrderItem.objects.get_or_create(cart_id=current_cart,
                product_supplier_id=prosup, defaults={'number': quantity})
        if not created:
            order_item.number = F('number') + quantity
        
        return redirect('cart:showcart')

# def finalize_cart(request):
#     if request.method == 'GET':
