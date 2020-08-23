from django.db import models
from accounts.models import Customer
from Supplier.models import ProductSupplier

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
    Purchase_Status_Choices = [
        ('u', 'Unfinilized'),
        ('f', 'Finalized'),
    ]
    customer_id = models.OneToOneField(Customer, on_delete=models.CASCADE)
    delivery_id = models.OneToOneField(Delivery, on_delete=models.CASCADE,null=True,blank=True)
    total_price = models.FloatField(default=0)
    status = models.CharField(max_length=1 ,choices=Purchase_Status_Choices, default='u')



class OrderItem(models.Model):
    """
    har itemi ke baraye kharid entekhab mishe va badan mire to cart
    """    
    cart_id = models.ForeignKey(Cart, related_name='order', on_delete=models.CASCADE)   
    product_supplier_id = models.ForeignKey(ProductSupplier, related_name= 'order',on_delete=models.CASCADE)
    cost = models.FloatField(default=0) #keeps/hold price constant, when car1t status was finalized
    number = models.IntegerField(default=0)

    def __str__(self):
        return str(self.cart_id.id)