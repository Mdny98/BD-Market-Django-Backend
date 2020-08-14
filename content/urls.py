from django.urls import path
from content import views


app_name = 'content'

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('products/<int:cat_pk>', views.products, name='products'),
    path('productdetails/<int:product_pk>', views.productdetails, name='productdetails'),
]