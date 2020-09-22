from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from . import views


router = routers.DefaultRouter()
router.register('product', views.ProductView)
router.register('category', views.CatView)
router.register('brand', views.BrandView)
router.register('attribute', views.AttributeView)
router.register('feedback', views.FeedbackView)
router.register('proattr', views.ProductAttrView)
router.register('customeraddress', views.CustomerAddressView)
router.register('customer', views.CustomerView)
router.register('supplier', views.SupplierView)
router.register('productsupplier', views.ProductSupplierView)
router.register('cart', views.CartView)
router.register('orderitem', views.OrderItemView, basename='order')



urlpatterns = [
    path('', include(router.urls)),
    path('/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
