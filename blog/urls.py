from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name_  = 'newtonapp'

urlpatterns = [
    
    path('', views.home, name="home"),
    path('blog', views.blogview, name="blog"),
    
    path('register/' , views.register, name="register"),
    path('login/', auth_views.login, {'template_name':'newtonapp/login.html'}, name='login')
]