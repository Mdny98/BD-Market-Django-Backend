from django.contrib import admin
from accounts.models import  User , Customer , Supplier


admin.site.register(Supplier)
admin.site.register(User)
admin.site.register(Customer)


