from django.db import models
from accounts.models import Customer


class SubCategory(models.Model):
    """
        Represent Categories & subCategories & subsub and so on of products like "Home Appliance"
        and "Electrical appliances" and "Refrigerator" with a self-referential foreign key
    """
    cat_name = models.CharField(max_length=50)
    # cat_description = models.TextField(
    #     max_length=1000, blank=True, null=True)
    # cat_image = models.ImageField(
    #     upload_to='content/images/', blank=True, null=True)
    parent_category = models.ForeignKey(
        "self", on_delete=models.SET_NULL, blank=True, null=True, related_name="child_categories")

    def __str__(self):
        return self.cat_name


class Brand(models.Model):
    """
        Represent brands like "LG" with a Foreignkey Relation to subcategory
    """
    brand_name = models.CharField(max_length=250 , verbose_name= "نام برند")
    subcategory_id = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.brand_name

class Attribute(models.Model):
    """
        Represent attributes of products
    """
    attr_title = models.CharField(max_length=50, blank=True, null=True , verbose_name= "ویژگی")
    subcategory_id = models.ForeignKey(
        SubCategory, related_name="attr", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.attr_title

class Product(models.Model):
    """
        Represent every single product like "yakhchal freezer emersan model barfak :D "
    """
    product_name = models.CharField(max_length=250, verbose_name= "نام محصول")
    product_description = models.TextField(
        max_length=1000, blank=True, null=True , verbose_name= "توضیحات محصول")
    product_image = models.ImageField(
        upload_to='content/images/', blank=True, null=True, verbose_name= "تصویر محصول")
    subcategory_id = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL, blank=True, null=True, verbose_name= "دسته بندی")
    brand_id = models.ForeignKey(
        Brand, on_delete=models.SET_NULL, blank=True, null=True, related_name='brand', verbose_name= "نام برند")
    attribute = models.ManyToManyField(Attribute, through='ProductAttr', verbose_name= "ویژگی")

    def __str__(self):
        return self.product_name




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
    product_id = models.ForeignKey(Product, related_name="pro_attr", on_delete=models.CASCADE)
    attr_id = models.ForeignKey(Attribute, related_name="pro_attr", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product_id} - {self.attr_id}'


class Feedback(models.Model):
    """
        Represent each user comment and rate to a specific product.
    """
    Rate_CHOICES = [
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****'),
    ]
    comment = models.TextField(max_length=250, blank=True, null=True)
    rate = models.IntegerField(choices=Rate_CHOICES, default=5)
    custumer_id = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    product_id = models.ForeignKey(
        Product, related_name="feedback", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.product_id} - {self.custumer_id}'
