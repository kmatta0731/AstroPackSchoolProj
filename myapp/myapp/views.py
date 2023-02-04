from django.shortcuts import render
from .login import login_view
from .register import register_view

def home(request):
    return render(request, 'index.html')
