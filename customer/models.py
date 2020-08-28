from django.db import models
from accounts.models import Customer
# Create your models here.
class CustomerAddress(models.Model):
   """
      Represent adresses of customers
   """
   address=city= models.CharField(max_length=250)
   customer_id=models.ForeignKey(Customer, on_delete=models.CASCADE)
   city= models.CharField(max_length=250)
   postalcode= models.IntegerField(blank=True, null=True)