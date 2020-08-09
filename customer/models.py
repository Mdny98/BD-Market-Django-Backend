from django.db import models

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
   phone= models.IntegerField(blank=True, null=True)

class CustomerAddress():
   """
      Represent adresses of customers
   """
   address=city= models.CharField(max_length=250)
   customer_id=models.ForeignKey(CustomerProfile, on_delete=models.SET_NULL)
   city= models.CharField(max_length=250)
   postalcode= models.IntegerField(blank=True, null=True)