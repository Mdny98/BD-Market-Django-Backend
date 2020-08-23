from django.db import models
from django.utils import timezone


class Article(models.Model):
    status_choices = [
        ('p', 'Published'),
        ('np', 'NotPublished')
    ]  


    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255,unique=True,allow_unicode=True)
    description = models.TextField()
    image = models.ImageField(upload_to="blog/images")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2 , choices= status_choices)


    def __str__(self):
        return self.title