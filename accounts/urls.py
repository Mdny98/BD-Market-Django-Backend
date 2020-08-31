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
    path('profile/', views.Profile.as_view(), name="profile"),



    path('buyhistory/', views.buyhistory, name='buyhistory'),
    path('stock/', views.StockList.as_view(), name='stock-list'),


    path('deletestock/<int:pk>', views.stockdelete.as_view(), name='delete-stock'),
    path('editpricestock/<int:pk>', views.editpricestock.as_view(), name='editpricestock'),
    path('editMojodi/<int:pk>', views.editMojodiestock.as_view(), name='editMojodiestock'),

# خراب
    path('confirmstock/', views.ConfrimCreate.as_view(), name='confirm-stock'),
    path('addstock/', views.stoockCreate.as_view(), name='add-stock'),



]