from django.contrib import admin
from accounts.models import  User , Customer , Supplier
from django.contrib.auth.admin import UserAdmin

admin.site.register(Supplier)
admin.site.register(User , UserAdmin)
admin.site.register(Customer)


