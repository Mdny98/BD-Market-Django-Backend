from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def singup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'registration/singup.html',{'form': form})




    form = UserCreationForm()
    return render(request, 'registration/singup.html',{'form': form})




def logout(request):
    logout(request)
    return redirect('content')





