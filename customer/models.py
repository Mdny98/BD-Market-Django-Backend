from django.db import models
from accounts.models import Customer
# Create your models here.
class CustomerAddress(models.Model):
   """
      Represent adresses of customers
   """
   address = models.CharField(max_length=250 , verbose_name='آدرس')
   customer_id =models.ForeignKey(Customer, on_delete=models.CASCADE )
   city = models.CharField(max_length=250 , verbose_name='شهر')
   postalcode= models.IntegerField(blank=True, null=True , verbose_name='کد پستی')