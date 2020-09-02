from django.urls import path
from . import  views



app_name = 'accounts'

urlpatterns=[

# هر ویو به ترتیب حضور در اینجا در قسمت ویوها هست


# قسمت ثبت نام


    # در اینجا صفحه ای هست که کاربر انتخاب میکنه فروشنده باشه یا خریدار
    path('register/',views.register, name='register'),
    # کاربر به صفحه ثبت نام به عنوان فروشنده هدایت میشه
    path('supplier_register/',views.SupplierRegister.as_view(), name='supplier_register'),
    # کاربر به صفحه ثبت نام به عنوان خریدار منتقل میشه
    path('customer_register/',views.CustomerRegister.as_view(), name='customer_register'),
    # پس از ثبت نام به این صفحه منتقل میشه که میگه ایمیلی براش ارسال شده
    path('registersen-mail/',views.registersendmail, name='registersendmail'),
    # پس از تکمیل ثبت نام و کلیک رو دکمه داشبورد به اینجا فرستاده میشود که پر است از فانکشنالیتی
    path('profile/', views.Profile.as_view(), name="profile"),
    

 
#قسمت مقالات 
 
    #اینجا هر کاربر لیست مقالات خودش را میبیند ولی سوپر یوزر می تواند همه مقالات موجود در سایت رو در اینجا ببیند و با توجه به دکه هایی که تعبیه شده امکان ححذف یا ویرایش انها را دارد
    path('', views.ArticleList.as_view(), name='home'),
    # در اینجا هر کاربر می تواند مقاله ارسال کند ولی وضعیت این مقاله همیشه پیشنویس است و تا تایید ادمین در سایت نمایش داده نمیشود
    path('article/create/', views.ArticleCreate.as_view(), name="article-create"),
    # در اینجا می توان مقاله را اصلاح تمود
    path('article/update/<int:pk>', views.ArticleUpdate.as_view(), name="article-update"),
    # در اینجا هم مقاله حذف میشود
    path('article/delete/<int:pk>', views.ArticleDelete.as_view(), name="article-delete"),
    

# قسمت خریدار

    # در این قسمت خریدار ادرس جدیدی اضافه میکند 
    path('addrescostomeradd/', views.addrescostomeradd.as_view(), name="addrescostomeradd"),
    # در اینجا خریدار تمام ادرس های خودش رو می تونه ببینه
    path('addrescostomershow/', views.addrescostomershow.as_view(), name="addrescostomershow"),
    # در اینجا ادرس حذف میشود
    path('adrrsssdelete/<int:pk>', views.adrrsssdelete.as_view(), name="adrrsssdelete"),
    # در اینجا ادرس اصلاح میشود
    path('addrescostomerupdate/<int:pk>', views.addrescostomerupdate.as_view(), name="addrescostomerupdate"),
    # در اینجا مشتری تاریخچه خرید خودش را میبیند
    path('buyhistory/', views.buyhistory, name='buyhistory'),



# قسمت فروشنده
    
    # در این قسمت فروشنده تمامی اجناس موجود در سایتش را میبیند
    path('stock/', views.StockList.as_view(), name='stock-list'),
    # در اینجا می تواند تعداد اجناس را کم یا زیاد نماید
    path('editMojodi/<int:pk>', views.editMojodiestock.as_view(), name='editMojodiestock'),
    # در اینجا می تواند ان محصول را حذف کند
    path('deletestock/<int:pk>', views.stockdelete.as_view(), name='delete-stock'),
    # در اینجا می تواند قیمت محصول را عوض کند
    path('editpricestock/<int:pk>', views.editpricestock.as_view(), name='editpricestock'),
    # در اینجا می تواند محصولی را اضافه نماید
    path('addstock/', views.stoockCreate.as_view(), name='add-stock'),
    # پس از اضافه کردن محصول در اینجا محصول را تایید نهایی می کند و مقادیر قیمت و تعداد که منحصر به فرد اوست را تغییر میدهد
    # در ضمن فروشنده مستقیما اجناسی که در فروشگاه هستند را از این مسیر اعلام امادگی فروش کند ودیگر نیازی به تعریف جنس نیست
    path('confirmstock/', views.ConfrimCreate.as_view(), name='confirm-stock'),
    # در اینجا برای محصول ویژگی تعیین میکند
    path('addattribute/', views.AddAttribute.as_view(), name='addattr'),
    # در اینجا یک برند تعیین میکند
    path('addbrand/', views.addbrand.as_view(), name='addbrand'),
    # 
    # path('productattr/', views.ProductAttr.as_view(), name='ProductAttr'),
]