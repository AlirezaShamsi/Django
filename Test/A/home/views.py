from django import http
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def say_hello(request):
    return render(request, 'hello.html')
# Create your views here.
