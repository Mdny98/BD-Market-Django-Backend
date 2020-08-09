from django.db import models
from django.contrib.auth.models import User
from customer.models import CustomerProfile
from Supplier.models import Product_Supplier

class Delivery(models.Model):
    """
    table sherkati ke peyk hast
    """    
    company_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)

    def __str__(self):
        return self.company_name



class Cart(models.Model):
    """
    sabad khraid
    """    
    customer_id = models.OneToOneField(CustomerProfile, on_delete=models.CASCADE)
    delivery_id = models.OneToOneField(Delivery, on_delete=models.CASCADE)
    total_price = models.FloatField(default=0)



class OrderItem(models.Model):
    """
    har itemi ke baraye kharid entekhab mishe va badan mire to cart
    """    
    cart_id = models.OneToOneField(Cart, on_delete=models.CASCADE)   
    product_supplier_id = models.OneToOneField(Product_Supplier, on_delete=models.CASCADE)
    price = models.ForeignKey(Product_Supplier.unit_price, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.cart_id