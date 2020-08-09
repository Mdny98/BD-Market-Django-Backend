from django.contrib import admin
from .models import  Delivery , Cart , OrderItem

admin.site.register(Delivery)
admin.site.register(Cart)
admin.site.register(OrderItem)
