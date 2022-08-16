from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('hello/', views.say_hello),
    path('detail/<int:todo_id>', views.detail, name = 'detail'),
    path('delete/<int:todo_id>', views.delete, name= 'delete'),
]