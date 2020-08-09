from django.db import models
from django.contrib.auth.models import User
from content.models import Product

# Create your models here.


class Supplier_Profile(models.Model):
    """
        a table for all supplier
    """
    city_choices = [
        ('tehran', 'Tehran'),
        ('ardebil', 'Ardebil'),
        ('rasht', 'Rasht'),
        ('kerman', 'Kerman'),
        ('ahvaz', 'Ahvaz')
    ]  # to baghie sharha namayandeghi nadarim
    supplier = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    address = models.TextField(max_length=500)
    city = models.CharField(max_length=50, choices=city_choices)

    def __str__(self):
        return self.company_name


class Product_Supplier(models.Model):
    """
    a table between products and supplier
    """
    supplier_id = models.ForeignKey(Supplier_Profile, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    unit_price = models.IntegerField(blank=True, null=True)
