from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CustomerProfile(models.Model):
   """
      Represent Customers Informations 
   """
   user_id = models.OneToOneField(User, on_delete= models.CASCADE)
   gender_choices = [
         ('M', 'Male'), 
         ('F', 'Female')
      ]
   gender = models.CharField(max_length=1, choices=gender_choices,blank=True, null=True)
   phone = models.IntegerField(blank=True, null=True)

class CustomerAddress(models.Model):
   """
      Represent adresses of customers
   """
   address=city= models.CharField(max_length=250)
   customer_id=models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
   city= models.CharField(max_length=250)
   postalcode= models.IntegerField(blank=True, null=True)