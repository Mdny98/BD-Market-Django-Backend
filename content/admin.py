from django.contrib import admin
from content import models
# Register your models here.
admin.site.register(models.SubCategory)
admin.site.register(models.Brand)
admin.site.register(models.Product)
admin.site.register(models.Attribute)
admin.site.register(models.ProductAttr)
admin.site.register(models.Feedback)

