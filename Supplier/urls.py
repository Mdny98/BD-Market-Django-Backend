from django.urls import path
from Supplier import views 

urlpatterns = [
    path('showall', views.show_all_suppliers, name='all_suppliers'),
    path('showall/<int:id>', views.show_supplier, name='supplier'),
]