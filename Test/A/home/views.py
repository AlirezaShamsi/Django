from django import http
from django.shortcuts import render

from .models import Todo

def home(request):
    all = Todo.objects.all()
    posts = {'posts':all,}
    return render(request, 'home.html', context=posts)

def say_hello(request):
    person = {'first': 'Alireza', 'two': 'Multiface',}
    return render(request, 'hello.html', context=person)
# Create your views here.
