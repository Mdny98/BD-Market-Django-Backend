from django.db import models
from accounts.models import User
from django.utils import timezone
from extensions.utils import jalali_converter
from django.utils.html import format_html
from django.urls import reverse
class ArticleManager(models.Manager):
	def published(self):
		return self.filter(status='p')




class Category(models.Model):
	parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children', verbose_name="زیردسته")
	title = models.CharField(max_length=200, verbose_name="عنوان دسته‌بندی")
	slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته‌بندی")
	status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
	position = models.IntegerField(verbose_name="پوزیشن")

	class Meta:
		verbose_name = "دسته‌بندی"
		verbose_name_plural = "دسته‌بندی ها"
		ordering = ['parent__id', 'position']

	def __str__(self):
		return self.title



class Article(models.Model):
    status_choices = [
        ('p', 'منتشر شده'),
        ('np', 'پیش نویس')
    ]
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles', verbose_name="نویسنده")  
    title = models.CharField(max_length=200,verbose_name = "عنوان")
    slug = models.SlugField(max_length=255,unique=True,allow_unicode=True , verbose_name = "آدرس مقاله")
    description = models.TextField(verbose_name = "متن")
    image = models.ImageField(upload_to="blog/images",verbose_name = "تصویر")
    publish = models.DateTimeField(default=timezone.now , verbose_name = "زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2 , choices= status_choices , verbose_name = "وضعیت")
    category = models.ManyToManyField(Category, verbose_name="دسته‌بندی", related_name="articles")
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ["-publish"]


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("accounts:home")
    
    def jpublish(self):
	    return jalali_converter(self.publish)
    jpublish.short_description = "زمان انتشار"
    
    def category_to_str(self):
	    return "، ".join([category.title for category in self.category.all()])
    category_to_str.short_description = "دسته‌بندی"

    def category_publish(self):
        return self.category.filter(status=True)
    
    def thumbnail_tag(self):
        return format_html("<img width=100 height=75 style='border-radius: 5px;' src='{}'>".format(self.image.url))
    thumbnail_tag.short_description = "عکس"	
    
    objects = ArticleManager()