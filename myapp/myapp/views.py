from datetime import datetime
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
        occasion = request.POST.get('occasion')
        start_date = request.POST.get('trip_start_date')
        end_date = request.POST.get('trip_end_date')
        gender = request.POST.get('gender')

         # Convert checkin and checkout strings to datetime objects
        checkin_date = datetime.strptime(start_date, '%Y-%m-%d')
        checkout_date = datetime.strptime(end_date, '%Y-%m-%d')

        # Calculate the number of days between the two dates
        num_days = (checkout_date - checkin_date).days

        #create the trip object based on user input
        trip = Trip (
            trip_userID=user, 
            trip_destination=destination, 
            trip_weather=temp, 
            occasion=occasion,
            trip_start_date=start_date,
            trip_end_date=end_date,
            gender=gender,
            num_days=num_days
        )
        trip.save()
        return JsonResponse({'status': 'success'})
    else:
        return HttpResponse("Error.")

def items(request):
    query_results = occasion.objects.all()
    query_results2 = Clothing.objects.all()
    context = {'occasion':query_results, 'Clothing': query_results2}
    return render(request,'items.html', context, )
   