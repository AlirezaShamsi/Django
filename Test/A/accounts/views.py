from ast import Pass
import re
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            user.firstname = cd['first_name']
            user.lastname = cd['last_name']
            user.save()
            messages.success(request, 'User registerd successfull', 'success')
            return redirect('home')

            

    else:
        form = UserRegistrationForm()
    return render(request, 'register.html' , {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login seccesfully', 'success')
                return redirect('home')
            else:
                messages.error(request, 'Username or Password are wrong', 'danger')

    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form':form})


def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully', 'info')
    return redirect('home')



# Create your views here.
