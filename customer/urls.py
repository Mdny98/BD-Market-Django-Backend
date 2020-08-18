from django.urls import path
from customer import views
from django.urls import path
from .views import custom_login, custom_logout


app_name = 'customer'

urlpatterns = [
    # path('register/', register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    # path('profile/', profile_show, name='profile'),
    # path('profile/edit', edit_profile, name='edit-profile'),
]
