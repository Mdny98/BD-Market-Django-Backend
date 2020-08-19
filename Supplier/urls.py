from django.urls import path
from Supplier import views 

urlpatterns = [
    path('singup', views.singup, name='singup'),
    
]