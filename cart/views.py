from django.shortcuts import render
from django.http import HttpResponse

from .models import Cart, OrderItem
from Supplier.models import ProductSupplier
# Create your views here.

from .models import Cart


def showcart(request):
    if request.method == 'GET':
        current_customer = request.user.customer
        current_cart = Cart.objects.get(customer_id=current_customer, status="u")
        
        return render(request, 'cart/showcart.html', {'current_cart':current_cart})

    if request.method == 'POST':
        current_customer = request.user.customer
        prosupid = request.POST.get('prosupid')
        # print(f'\nprosup_id is{prosup_id}')
        prosup = ProductSupplier.objects.get(pk=prosupid)
        current_cart, created = Cart.objects.get_or_create(
                                    customer_id=current_customer,
                                    status='u',)
        order_item = OrderItem(cart_id=current_cart, product_supplier_id=prosup, number=1)
        order_item.save()
        return render(request, 'cart/showcart.html')