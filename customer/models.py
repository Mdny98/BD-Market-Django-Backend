from django.db import models

# Create your models here.
class Customer(models.Model):
   """
      Represent Customers Informations 
   """
   firstname= models.CharField(max_length=250)
   lastname= models.CharField(max_length=250)
   city= models.CharField(max_length=250)
   postalcode= models.IntegerField(blank=True, null=True)
   phone= models.IntegerField(blank=True, null=True)
   email= models.CharField(max_length=250)
   username= models.CharField(max_length=250)
   password= models.IntegerField()
   dateentered= models.DateTimeField()