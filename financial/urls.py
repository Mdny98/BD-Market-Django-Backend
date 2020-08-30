from django.urls import path
from financial import views 

app_name = 'financial'

urlpatterns = [
    path('', views.finalize_cart, name='finalize_cart'),
    path('pay/', views.pay, name='pay'),
    path('thanks/', views.success_paid, name='success_paid'),
]