from django.contrib import admin
from blog.models import Article , Category
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin

def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated == 1:
        message_bit = "منتشر شد."
    else:
        message_bit = "منتشر شدند."
    modeladmin.message_user(request, "{} مقاله {}".format(rows_updated, message_bit))
make_published.short_description = "انتشار مقالات انتخاب شده"

def make_draft(modeladmin, request, queryset):
    rows_updated = queryset.update(status='np')
    if rows_updated == 1:
        message_bit = "پیش‌نویس شد."
    else:
        message_bit = "پیش‌نویس شدند."
    modeladmin.message_user(request, "{} مقاله {}".format(rows_updated, message_bit))
make_draft.short_description = "پیش‌نویس شدن مقالات انتخاب شده"




class CategoryAdmin(admin.ModelAdmin):
	list_display = ('position', 'title','slug', 'parent','status')
	list_filter = (['status'])
	search_fields = ('title', 'slug')
admin.site.register(Category, CategoryAdmin)



class ArticleAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ('title','thumbnail_tag','jpublish','status','category_to_str')
    list_filter = ('status','publish')
    search_fields = ('title','description')
    ordering = ('publish',)
    actions = [make_published, make_draft]
    
    
admin.site.register(Article , ArticleAdmin)


