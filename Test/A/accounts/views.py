from ast import Pass
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data()
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, 'User registerd successfull', 'success')
            return redirect('home')

            

    else:
        form = UserRegistrationForm()
    return render(request, 'register.html' , {'form': form})

# Create your views here.
