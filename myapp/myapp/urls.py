from django.contrib import admin
from django.urls import path, include
from myapp.views import home
from . import views
from django.urls import path
from user_dashboard.views import dashboard
from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home, name='home'),
    path('process_form/', views.process_form, name ='process_form'),
    path('dashboard/', dashboard, name='dashboard'),
    path('home', views.logout_view, name='logout'),
    path('process_temp/', views.process_temp, name='process_temp'),
]