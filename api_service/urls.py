from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('product', views.ProductView)
router.register('category', views.CatView)
router.register('brand', views.BrandView)


urlpatterns = [
    path('', include(router.urls))
]
