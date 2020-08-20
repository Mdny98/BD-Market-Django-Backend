from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required

from .models import CustomerProfile, CustomerAddress
from .forms import ProfileForm




class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email',
                  'password1', 'password2']
        labels = {
            "username": "نام کاربری",
            "email": "ایمیل",
            "password1": "رمز عبور",
            "password2": "تکرار رمز عبور",
        }

        help_texts = {
            'username': 'باید کمتر از 150 کاراکتر باشد',
            "email": "ایمیل خود را به درستی وارد کنید",
        }

    def save(self, commit=True):
        '''
        override user create form to create profile after register!
        '''
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        try:
            if commit:
                user.save()
            CustomerProfile.objects.create(user=user)

        except Exception as e:
            user.delete()
            raise ValueError(f"cant create profile object! reason: {e}")

        return user

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print(request.POST['username'])
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'registration/register.html', {'form': form})

    form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        if authenticate(username=username, password=password):
            user_obj = User.objects.get(username=username)
            login(request, user_obj)
            return redirect("content:home")
        else:
            return render(request, 'customer/login.html')

        print(request.POST)
    return render(request, 'customer/login.html')


@login_required(login_url='/login/')
def profile_show(request):
    if request.method == 'GET':
        # profile = CustomerProfile.objects.get(user=request.user)
        # address = profile.address_by.all()
        return render(request, 'customer/profile.html')
        return render(request, 'profile.html', {'profile': profile, 'address': address})


def custom_logout(request):
    logout(request)
    return redirect('content:home')


@login_required(login_url='login')
def edit_profile(request):
    profile = CustomerProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
        return redirect('profile')

    form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})
