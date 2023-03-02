from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from occasion.models import Trip
from myapp.forms import DestinationForm
from django import forms
from myapp.views import *
from myapp.models import *

@login_required
def dashboard(request):
    return render(request, 'user_dashboard/templates/dashboard.html',{'form': DestinationForm})

def saved_trips(request):
    return render(request, 'saved_trips.html')
