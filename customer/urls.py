from django.urls import path
from customer import views
from django.urls import path
from .views import custom_login, custom_logout , register ,profile_show


app_name = 'customer'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('profile/', profile_show, name='profile'),
    # path('profile/edit', edit_profile, name='edit-profile'),
]
