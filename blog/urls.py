from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import  BlogDetail
from . import views


urlpatterns = [
    
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blogs"),
    
    path('blog/<int:pk>/',  BlogDetail.as_view(), name='detail'),
    path('register/' , views.register, name="register"),
    path('login/', auth_views.login, {'template_name':'newtonapp/login.html'}, name='login')
]