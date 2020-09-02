from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView , ListView , UpdateView , DeleteView
from .form import CustomerSignUpForm, SupplierSignUpForm , ProfileForm , ConfrimForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Article
from Supplier.models import ProductSupplier
from accounts.mixin import FieldsMixin , FormValidMixin , SuperUserAccessMixin , AuthorsAccessMixin  , FormStockValidMixin 
from content.models import Product , Attribute , Brand , ProductAttr 
from django.urls import reverse_lazy
from accounts.models import User
from django.contrib.auth.views import PasswordChangeView 
from customer.models import CustomerAddress
from cart.models import Cart
from django_email_verification import sendConfirm

# توضیحات در قسمت یو ار ال امده است
# قسمت ثبت نام
# در اینجا صفحه ای هست که کاربر انتخاب میکنه فروشنده باشه یا خریدار
def register(request):
    return render(request, 'accounts/register.html')

class SupplierRegister(CreateView):
    model = User
    form_class = SupplierSignUpForm
    template_name = 'accounts/supplier_register.html'

    def form_valid(self, form):
        user = form.save()
        sendConfirm(user)
        # login(self.request, user)
        return redirect('accounts:registersendmail')

class CustomerRegister(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'accounts/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        sendConfirm(user)
        # login(self.request, user)
        return redirect('accounts:registersendmail')

def registersendmail(request):
    return render(request, 'accounts/afterrejister.html')



class Profile(UpdateView):
    model = User
    template_name = "registration/profile.html"
    form_class = ProfileForm
    
    success_url = reverse_lazy("accounts:profile")
    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)
    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
			'user': self.request.user
		})
        return kwargs





#قسمت مقالات 
class ArticleList(LoginRequiredMixin , ListView):
    template_name = "registration/home.html"
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)


class ArticleCreate(LoginRequiredMixin, FormValidMixin, FieldsMixin, CreateView):
	model = Article
	template_name = "registration/article-create-update.html"



class ArticleUpdate(LoginRequiredMixin, FormValidMixin, FieldsMixin, UpdateView):
	model = Article
	template_name = "registration/article-create-update.html"

class ArticleDelete(SuperUserAccessMixin , DeleteView):
	model = Article
	success_url = reverse_lazy('accounts:home')
	template_name = "registration/article_confirm_delete.html"







# قسمت خریدار

class addrescostomeradd(LoginRequiredMixin, CreateView):
    model = CustomerAddress
    fields = ['address', 'city', 'postalcode']
    template_name = "registration/addadress.html" 
    success_url = reverse_lazy('accounts:addrescostomershow')
    def form_valid(self, form):
        d = form.save(commit=False)
        d.customer_id = self.request.user.customer
        d.save()
        return super().form_valid(form)




class addrescostomershow(LoginRequiredMixin , ListView):
    template_name = "registration/Alladress.html"
    def get_queryset(self):
        return CustomerAddress.objects.filter(customer_id=self.request.user.customer)



class addrescostomerupdate(LoginRequiredMixin, UpdateView):
    model = CustomerAddress
    fields = ['address', 'city', 'postalcode']
    template_name = "registration/addadress.html"
    success_url = reverse_lazy('accounts:addrescostomershow')

class adrrsssdelete(LoginRequiredMixin, DeleteView):
    model = CustomerAddress
    success_url = reverse_lazy('accounts:addrescostomershow')
    template_name = "registration/addresstock.html"



def buyhistory(request):

    if request.method=='GET':
        current_customer = request.user.customer
        carts = Cart.objects.filter(customer_id=current_customer, status="f")

        return render(request, 'accounts/buyhistory.html', {'carts':carts})







# قسمت فروشنده

class StockList(LoginRequiredMixin , ListView):
    template_name = "registration/AllStock.html"
    def get_queryset(self):
        return ProductSupplier.objects.filter(supplier_id=self.request.user.supplier)

class editpricestock(LoginRequiredMixin,UpdateView):
    model = ProductSupplier
    fields = ['unit_price']
    success_url = reverse_lazy('accounts:stock-list')
    template_name = "registration/editpricestock.html"

class stockdelete(LoginRequiredMixin, DeleteView):
    model = ProductSupplier
    success_url = reverse_lazy('accounts:stock-list')
    template_name = "registration/deletstock.html"


class stoockCreate(LoginRequiredMixin, CreateView):
    model = Product
    fields = [
			"product_name", "product_description", "product_image",
			"subcategory_id", "brand_id", "attribute"
		]
    success_url = reverse_lazy('accounts:confirm-stock')
    template_name = "registration/addstock.html"
    
class AddAttribute(LoginRequiredMixin, CreateView):
    model = Attribute
    fields = ["attr_title"]
    success_url = reverse_lazy('accounts:add-stock')
    template_name = "registration/AddAttribute.html"

class ProductAttr(LoginRequiredMixin, CreateView):
    model = ProductAttr
    fields = ["value_type","int_value","text_value","bool_value","product_id",'attr_id']
    success_url = reverse_lazy('accounts:add-stock')
    template_name = "registration/ProductAttr.html"
    


class addbrand(LoginRequiredMixin, CreateView):
    model = Brand
    fields = ["brand_name"] 
    success_url = reverse_lazy('accounts:add-stock')
    template_name = "registration/addbrand.html"



class ConfrimCreate(LoginRequiredMixin, CreateView):
    model = ProductSupplier
    fields = ['product_id', 'unit_price', 'stock']
   


    template_name = "registration/confrmstock.html" 
    success_url = reverse_lazy('accounts:stock-list')
    def form_valid(self, form):
        if not self.request.user.is_superuser:
            d = form.save(commit=False)
            d.supplier_id = self.request.user.supplier
            d.save()
            return super().form_valid(form)
        









# در اینجا دو صفحه شخصی شده تغییر پسورود و تایید ان را نمایش میدهد
class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy('accounts:password_change_done')

def PasswordChangeDoneView(request):
    return render(request, 'accounts/v.html')








# دو تابع زیر کار ورود و خروج را انجام می دهند 
def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('accounts:profile')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'registration/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')
