from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter

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
    
    def jpublish(self):
	    return jalali_converter(self.publish)
    jpublish.short_description = "زمان انتشار"
    
    def category_to_str(self):
	    return "، ".join([category.title for category in self.category.all()])
    category_to_str.short_description = "دسته‌بندی"

    def category_publish(self):
        return self.category.filter(status=True)
    
    objects = ArticleManager()