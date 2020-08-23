from django.contrib import admin
from blog.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','publish','status')
    list_filter = ('status','publish')
    search_fields = ('title','description')
    ordering = ('publish',)

admin.site.register(Article , ArticleAdmin)