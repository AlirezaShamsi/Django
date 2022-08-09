from django import http
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def say_hello(request):
    person = {'first': 'Alireza', 'two': 'Multiface',}
    return render(request, 'hello.html', context=person)
# Create your views here.
