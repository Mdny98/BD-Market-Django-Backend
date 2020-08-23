from django.urls import path
from blog import views


app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<slug:slug>', views.detail, name='detail'),
]