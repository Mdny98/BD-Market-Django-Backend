from django.urls import path
from Supplier import views 


app_name = 'Supplier'
urlpatterns = [
    path('singup/', views.singup, name='singup'),
    
]