from django.db import models
from content.models import Product
from accounts.models import Supplier

# Create your models here.



class ProductSupplier(models.Model):
    """
    a table between products and supplier
    """
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplier', verbose_name= "نام خریدار")
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name= "نام محصول")
    stock = models.IntegerField(default=0, verbose_name= "تعداد")
    unit_price = models.FloatField(blank=True, null=True, verbose_name= "قیمت")
