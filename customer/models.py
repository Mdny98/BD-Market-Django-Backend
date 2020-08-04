from django.db import models

# Create your models here.
class Customer(models.Model):
     """
        Represent Customers Informations 
     """
    firstname= models.CharField(max_length=250)
    lastname= models.CharField(max_length=250)
    city= models.CharField(max_length=250)
    postalcode= models.IntegerField(max_length=250)
    phone= models.IntegerField(max_length=250)
    email= models.CharField(max_length=250)
    username= models.CharField(max_length=250)
    password= models.IntegerField(max_length=250)
    dateentered= models.DateTimeField(max_length=250)