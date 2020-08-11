from django.db import models
from cart.models import Cart

# Create your models here.


class PeymentMethod(models.Model):
    """
    identify Payment method
    """
    method_title = models.CharField(max_length=250)


class Payment(models.Model):
    """
        Represent Payment history records
    """
    payment_status = models.BooleanField()
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(
        PeymentMethod, on_delete=models.SET_NULL, blank=True, null=True)
    
