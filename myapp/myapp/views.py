from django.shortcuts import render
from .login import login_view
from .register import register_view
from .forms import process_form
from user_dashboard.views import dashboard
from .logout import logout_view

def home(request):
    return render(request, 'index.html')
