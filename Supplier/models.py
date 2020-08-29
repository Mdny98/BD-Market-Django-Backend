from django.db import models
from content.models import Product
from accounts.models import Supplier

# Create your models here.



class ProductSupplier(models.Model):
    """
    a table between products and supplier
    """
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplier')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    unit_price = models.FloatField(blank=True, null=True)
