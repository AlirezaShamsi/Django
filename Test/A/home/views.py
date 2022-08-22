from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm, TodoUpdateForm




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

def create(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title = cd['title'], body = cd['body'], created = cd['created'])
            messages.success(request, 'Todo created successfully', 'success')
            return redirect('home')
    else:
        form = TodoCreateForm()
    return render(request, 'create.html', {'form': form})



def update(request, todo_id):
    if request.method == 'POST':
        pass
    else:
        form = TodoUpdateForm()
    return render(request, 'update.html', {'form': form})
