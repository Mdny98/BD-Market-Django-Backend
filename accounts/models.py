from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100, verbose_name="نام")
    last_name = models.CharField(max_length=100 , verbose_name="نام خانوادگی")
    
    

gender_choices = [
         ('M', 'Male'), 
         ('F', 'Female')
      ]
city_choices = [
        ('tehran', 'Tehran'),
        ('ardebil', 'Ardebil'),
        ('rasht', 'Rasht'),
        ('kerman', 'Kerman'),
        ('ahvaz', 'Ahvaz')
    ]  

    
class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='customer', on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20, verbose_name= "شماره تلفن همراه")
    gender = models.CharField(max_length=50, choices=gender_choices, verbose_name='جنسیت')
    city = models.CharField(max_length=50, choices=city_choices , verbose_name= "شهر")


class Supplier(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='supplier', on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20,verbose_name= "شماره تلفن همراه")
    company_name = models.CharField(max_length=50,verbose_name= "نام شرکت")
    address = models.TextField(max_length=500)
    city = models.CharField(max_length=50, choices=city_choices)

    def __str__(self):
        return self.company_name


