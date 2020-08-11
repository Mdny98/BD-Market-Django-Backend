from django.db import models
from customer.models import CustomerProfile


class SubCategory(models.Model):
    """
        Represent Categories & subCategories & subsub and so on of products like "Home Appliance"
        and "Electrical appliances" and "Refrigerator" with a self-referential foreign key
    """
    cat_name = models.CharField(max_length=50)
    parent_category = models.ForeignKey(
        "self", on_delete=models.SET_NULL, blank=True, null=True, related_name="child_categories")

    def __str__(self):
        return self.cat_name


class Brand(models.Model):
    """
        Represent brands like "LG" with a Foreignkey Relation to subcategory
    """
    brand_name = models.CharField(max_length=250)
    subcategory_id = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    """
        Represent every single product like "yakhchal freezer emersan model barfak :D "
    """
    product_name = models.CharField(max_length=250)
    product_description = models.TextField(
        max_length=1000, blank=True, null=True)
    
    image = models.ImageField(
        upload_to='content/images/', blank=True, null=True)
    subcategory_id = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL, blank=True, null=True)
    brand_id = models.ForeignKey(
        Brand, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.product_name


class Attribute(models.Model):
    """
        Represent attributes of products
    """
    attr_title = models.CharField(max_length=50, blank=True, null=True)
    subcategory_id = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.attr_title

class ProductAttr(models.Model):
    """
        Handle products attributes
    """
    Value_Type_CHOICES = [
        ('INT', 'Integer'),
        ('TXT', 'Text'),
        ('BOOL', 'Bool'),
    ]
    value_type = models.CharField(max_length=4, choices=Value_Type_CHOICES)
    int_value = models.IntegerField(blank=True, null=True)
    text_value = models.TextField(max_length=250, blank=True, null=True)
    bool_value = models.BooleanField(blank=True, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    attr_id = models.ForeignKey(Attribute, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product_id} - {self.attr_id}'

class Feedback(models.Model):
    """
        Represent each user comment and rate to a specific product.
    """
    Rate_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    comment = models.TextField(max_length=250, blank=True, null=True)
    rate = models.IntegerField(choices=Rate_CHOICES, default=5)
    custumer_id = models.ForeignKey(CustomerProfile, on_delete=models.SET_NULL, blank=True, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.product_id} - {self.custumer_id}'