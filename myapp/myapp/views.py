import json
from django.shortcuts import redirect, render
from .login import login_view
from .register import register_view
from .forms import process_form
from user_dashboard.views import dashboard
from .logout import logout_view
from django import forms
from .forms import DestinationForm
from django.http import HttpResponse, JsonResponse

def home(request):
    return render(request, 'index.html', {'form': DestinationForm})

def process_temp(request):
    if request.method == 'POST':
        temp = request.POST.get('temp')
        print(request.body)
        return JsonResponse({'status': 'success'})
    else:
        print(request.body)
        return HttpResponse("This endpoint only accepts POST requests.")
