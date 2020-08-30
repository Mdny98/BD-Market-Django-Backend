from django.urls import path
from . import  views



app_name = 'accounts'

urlpatterns=[
    path('register/',views.register, name='register'),
    path('customer_register/',views.CustomerRegister.as_view(), name='customer_register'),
    path('supplier_register/',views.SupplierRegister.as_view(), name='supplier_register'),
    path('', views.ArticleList.as_view(), name='home'),
    path('article/create/', views.ArticleCreate.as_view(), name="article-create"),
    path('article/update/<int:pk>', views.ArticleUpdate.as_view(), name="article-update"),
    path('article/delete/<int:pk>', views.ArticleDelete.as_view(), name="article-delete"),
    path('stock/', views.StockList.as_view(), name='stock-list'),
    path('buyhistory/', views.buyhistory, name='buyhistory'),
    path('addstock/', views.stoockCreate.as_view(), name='add-stock'),
    path('confirmstock/', views.stoockConfrimCreate.as_view(), name='confirm-stock'),
    path('profile/', views.Profile.as_view(), name="profile"),
     
]