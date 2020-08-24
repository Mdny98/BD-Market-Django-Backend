from django.contrib import admin
from blog.models import Article , Category
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('position', 'title','slug', 'parent','status')
	list_filter = (['status'])
	search_fields = ('title', 'slug')
admin.site.register(Category, CategoryAdmin)



class ArticleAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ('title','jpublish','status','category_to_str')
    list_filter = ('status','publish')
    search_fields = ('title','description')
    ordering = ('publish',)
    
    
admin.site.register(Article , ArticleAdmin)