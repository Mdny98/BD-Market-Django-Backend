from django.urls import path
from financial import views 

app_name = 'financial'

urlpatterns = [
    path('', views.finalize_cart, name='finalize_cart'),
    path('thanks/', views.success_paid, name='success_paid'),
]