"""BDMarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404 , handler500
import content
from accounts.views import login_request , logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comment/', include('comment.urls')),
    path('login/',login_request, name='login'),
    path('', include('django.contrib.auth.urls')),
    path('logout/',logout_view, name='logout'),
    path('', include('content.urls'), name='content'),
    path('supplier/', include('Supplier.urls'), name='supplier'),
    path('cart/', include('cart.urls'), name='cart'),    
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('fin/', include('financial.urls'), name='financial'),
    path('blog/', include('blog.urls'), name='blog')
]
handler404 = content.views.error_404
handler500 = content.views.error_500
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "پنل ادمین بی دی "
admin.site.site_title = "صفحه شخصی ادمین بی دی"
admin.site.index_title = "خوش اومدید بزرگوار"