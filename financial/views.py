from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import F
from django.contrib.auth.decorators import login_required

from .models import PeymentMethod, Payment
from cart.models import Cart, OrderItem
from customer.models import CustomerAddress


# Create your views here.

@login_required
def finalize_cart(request):
    try:
        current_customer = request.user.customer
        current_cart = Cart.objects.get(customer_id=current_customer, status="u")
        orders = current_cart.order.all()
    except:
        return render(request, 'financial/pay.html', {'msg':'شما فاکتور ثبت شده ای ندارید'})

    payment_methods = PeymentMethod.objects.all
    total_price = 0
    if request.method == 'POST':
                 
        for order in orders:
            order.number = int(request.POST.get(str(order.id)))
            # print(order.number)
            # print(type(order.number))

            total_price += order.number * order.product_supplier_id.unit_price
            order.save()

        return render(request, 'financial/pay.html', {'payment_methods':payment_methods,
         'total_price':total_price})

    else:
        for order in orders:
            total_price += order.number * order.product_supplier_id.unit_price

        return render(request, 'financial/pay.html', {'payment_methods':payment_methods,
            'total_price':total_price})

@login_required
def pay(request):
    if request.method == 'POST':
        try:
            address_id = request.POST['address']
        except:
            payment_methods = PeymentMethod.objects.all
            return render(request, 'financial/pay.html', {'payment_methods':payment_methods, 'err':'یک آدرس ثبت کنید'})
        payment_method_id = request.POST['payment_method']
        payment_method = PeymentMethod.objects.get(id=payment_method_id)
        current_customer = request.user.customer
        current_cart = Cart.objects.get(customer_id=current_customer, status="u")
        payment, created = Payment.objects.get_or_create(cart_id=current_cart,
                                defaults={'payment_status': False, 'payment_method':payment_method})
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
                current_prosup = order.product_supplier_id
                current_prosup.stock = F('stock') - order.number
                current_prosup.save()
                total += order.number * order.cost
                order.save()

            address_id = request.POST['address']
            address = CustomerAddress.objects.get(id=address_id)
            current_cart.adresses = address
            current_cart.status = 'f'
            current_cart.total_price = total
            current_cart.save()

            return redirect('financial:success_paid')

@login_required
def success_paid(request):
    return HttpResponse('thank you')