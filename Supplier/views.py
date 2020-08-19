from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , logout
from django.contrib.auth.forms import UserCreationForm



def singup(request):
    form = UserCreationForm()
    return render(request, 'registration/singup.html',{'form': form})




def logout(request):
    logout(request)
    return redirect('content')
