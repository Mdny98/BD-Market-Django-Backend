from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView , ListView , UpdateView
from .form import CustomerSignUpForm, SupplierSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Article
from Supplier.models import ProductSupplier
from accounts.mixin import FieldsMixin , FormValidMixin
# @login_required
# def home(request):
#     return render(request, 'registration/home.html')

class ArticleList(LoginRequiredMixin , ListView):
    template_name = "registration/home.html"
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)

class ArticleCreate(LoginRequiredMixin, FormValidMixin , FieldsMixin, CreateView):
	model = Article
	template_name = "registration/article-create-update.html"


class ArticleUpdate(LoginRequiredMixin, FormValidMixin, FieldsMixin, UpdateView):
	model = Article
	template_name = "registration/article-create-update.html"




def register(request):
    return render(request, 'accounts/register.html')

class CustomerRegister(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'accounts/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class SupplierRegister(CreateView):
    model = User
    form_class = SupplierSignUpForm
    template_name = 'accounts/supplier_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('accounts:home')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'registration/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')



class StockList(LoginRequiredMixin , ListView):
    template_name = "registration/AllStock.html"
    def get_queryset(self):
        return ProductSupplier.objects.filter(supplier_id=self.request.user)