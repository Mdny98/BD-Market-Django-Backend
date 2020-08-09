from django.urls import path
from cart import views 

urlpatterns = [
    path('cart', views.cart, name='cart'),
]