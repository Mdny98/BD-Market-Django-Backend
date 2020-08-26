from django.urls import path
from blog import views


app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('page/<int:page>', views.home, name='home'),
    path('category/<slug:slug>', views.category, name='category'),
    path('category/<slug:slug>/page/<int:page>', views.category, name='category'),
    path('article/<slug:slug>', views.detail, name='detail'),
]

