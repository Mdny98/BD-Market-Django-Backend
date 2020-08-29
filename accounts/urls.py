from django.urls import path
from . import  views



app_name = 'accounts'

urlpatterns=[
    path('register/',views.register, name='register'),
    path('customer_register/',views.CustomerRegister.as_view(), name='customer_register'),
    path('supplier_register/',views.SupplierRegister.as_view(), name='supplier_register'),
    path('login/',views.login_request, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('', views.ArticleList.as_view(), name='home'),
    path('article/create/', views.ArticleCreate.as_view(), name="article-create"),
    path('article/update/<int:pk>', views.ArticleUpdate.as_view(), name="article-update"),
    path('stock/', views.StockList.as_view(), name='stock-list'),
    
    
]