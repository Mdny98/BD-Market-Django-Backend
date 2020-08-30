from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import PeymentMethod, Payment
from cart.models import Cart, OrderItem

# Create your views here.

def finalize_cart(request):
    if request.method == 'POST':
        payment_methods = PeymentMethod.objects.all
        current_customer = request.user.customer
        current_cart = Cart.objects.get(customer_id=current_customer, status="u")
        orders = current_cart.order.all()
                 
        total_price = 0
        for order in orders:
            order.number = int(request.POST.get(str(order.id)))
            print(order.number)
            print(type(order.number))

            total_price += order.number * order.product_supplier_id.unit_price
            order.save()

        return render(request, 'financial/pay.html', {'payment_methods':payment_methods, 'total_price':total_price})

def pay(request):
    if request.method == 'POST':
        payment_method_id = request.POST['payment_method']
        payment_method = PeymentMethod.objects.get(id=payment_method_id)
        current_customer = request.user.customer
        current_cart = Cart.objects.get(customer_id=current_customer, status="u")
        payment, created = Payment.objects.get_or_create(payment_status=False, cart_id=current_cart,
                                payment_method=payment_method)
        # payment.save()

        transaction_result = True

        if transaction_result == True:
            current_customer = request.user.customer
            current_cart = Cart.objects.get(customer_id=current_customer, status="u")
            payment = Payment.objects.get(cart_id = current_cart)
            payment.payment_status = True
            payment.save()

            total = 0
            for order in current_cart.order.all():
                order.cost = order.product_supplier_id.unit_price
                total += order.number * order.cost
                order.save()

            current_cart.status = 'f'
            current_cart.total_price = total
            current_cart.save()

            return redirect('financial:success_paid')


def success_paid(request):
    return HttpResponse('thank you')