from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404 , handler500
import content
from accounts.views import login_request , logout_view
from django_email_verification import urls as mail_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login_request, name='login'),
    # با استفاده از کد زیر می تونیم از تابع های نوشته شده برای عوض کردن پسورد و بقیه چیزها استفاده کنیم
    path('', include('django.contrib.auth.urls')),
    # لاگ اوت کردن
    path('logout/',logout_view, name='logout'),
    # صفحه اصلی سایت
    path('', include('content.urls'), name='content'),
    path('cart/', include('cart.urls'), name='cart'),
    # بخش اکانت ها که تمامی کارهای مربوط به پروفایل در اینجا رخ می دهد
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('fin/', include('financial.urls'), name='financial'),
    # بخش بلاگ که به شدت کامله :)
    path('blog/', include('blog.urls'), name='blog'),
    #برای ارسال ایمیل فعالسازی اکانت
    path('email/', include(mail_urls)),
]

# تو این قسمت ارور ۴۰۴ رو هندل میکنیم و جای ویوش رو میگیم
handler404 = content.views.error_404
handler500 = content.views.error_500
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# این قسمت هم متن های پنل ادمین رو شخصی سازی میکنیم
admin.site.site_header = "پنل ادمین بی دی "
admin.site.site_title = "صفحه شخصی ادمین بی دی"
admin.site.index_title = "خوش اومدید بزرگوار"