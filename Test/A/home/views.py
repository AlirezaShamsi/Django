from django.shortcuts import render,redirect
from django.contrib import messages

from .models import Todo

def home(request):
    all = Todo.objects.all()
    posts = {'posts':all,}
    return render(request, 'home.html', context=posts)

def say_hello(request):
    person = {'first': 'Alireza', 'two': 'Multiface',}
    return render(request, 'hello.html', context=person)
# Create your views here.

def detail(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    return render(request, 'detail.html', {'todo' : todo})\

def delete(request, todo_id):
    Todo.objects.get(id = todo_id).delete()
    messages.success(request, 'Messsage has been deleted', 'warning')
    return redirect('home')
