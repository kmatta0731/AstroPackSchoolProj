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
from django.contrib.auth.decorators import user_passes_test
from occasion.models import *
def home(request):
    return render(request, 'index.html',{'form': DestinationForm})

def process_data(request):
    if request.method == 'POST':
        temp = request.POST.get('temp')
        destination = request.POST.get('destination')
        user = request.user
        trip = Trip(trip_userID=user, trip_destination=destination)
        trip.save()
        return JsonResponse({'status': 'success'})
    else:
        return HttpResponse("Error.")

def items(request):
    query_results = occasion.objects.all()
    query_results2 = Clothing.objects.all()
    context = {'occasion':query_results, 'Clothing': query_results2}
    return render(request,'items.html', context, )
   