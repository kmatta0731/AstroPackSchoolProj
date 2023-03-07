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
from django.contrib.auth.decorators import user_passes_test, login_required
from occasion.models import *
from .packing_list import *
from user_dashboard.saved_trips import *

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
        temp_range = request.POST.get('temp_range')
        activities = request.POST.getlist('activities')  # retrieve a list of selected activities

         # convert checkin and checkout strings to datetime objects
        checkin_date = datetime.strptime(start_date, '%Y-%m-%d')
        checkout_date = datetime.strptime(end_date, '%Y-%m-%d')

        # calculate the number of days between the two dates
        num_days = (checkout_date - checkin_date).days

        # create the trip object based on user input
        trip = Trip (
            trip_userID=user, 
            trip_destination=destination, 
            trip_weather=temp, 
            occasion=occasion,
            trip_start_date=start_date,
            trip_end_date=end_date,
            gender=gender,
            length_of_trip=num_days,
            temp_range=temp_range,
        )

        trip.save()

        for name in activities:
            activity, created = Activities.objects.get_or_create(name=name)
            trip.activities.add(activity)

        packing_list = generate_packing_list(trip)
        return render(request, 'items.html', {'packing_list': packing_list})

    else:
        return HttpResponse("Error.")

def items(request):
    trip = Trip.objects.filter(trip_userID=request.user).latest('id')
    packing_list = generate_packing_list(trip)
    context = {'packing_list': packing_list}
    print(packing_list)
    
    return render(request, 'items.html', context)

def saved_trips(request):
    user_id = request.user.id
    trips = Trip.objects.filter(trip_userID=user_id).order_by('-id')
    return render(request, "user_dashboard/templates/saved_trips.html", {'trips': trips})


def saved_list(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    saved_list = Generated_list.objects.filter(gen_tripID=trip).first()
    if saved_list:
        print(saved_list.gen_clothing.all())  # debug code
        clothing_items = saved_list.gen_clothing.all()
        comfort_items = saved_list.gen_comfort.all()
        accessory_items = saved_list.gen_accessories.all()
        toiletry_items = saved_list.gen_toiletries.all()
        health_items = saved_list.gen_health.all()
        equipment_items = saved_list.gen_equipment.all()
        shoe_items = saved_list.gen_shoe.all()
        essential_items = saved_list.gen_essentials.all()


        context = {'saved_list': saved_list}
        return render(request, 'saved_list.html', context)
    else:
        return HttpResponse("Error: no saved list found.")
