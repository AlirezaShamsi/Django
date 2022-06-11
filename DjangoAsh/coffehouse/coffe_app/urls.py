from django.urls import path, re_path
from . import views
urlpatterns = [
    path('homepage/', views.show_home_page),
]