from django.urls import path
from cart import views 

app_name = 'cart'

urlpatterns = [
    path('', views.showcart, name='showcart'),
    path('<int:order_pk>/delete', views.delete_order, name='delete_order'),
]