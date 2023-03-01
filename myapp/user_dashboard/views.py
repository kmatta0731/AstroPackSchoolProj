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
    # logic for saved trips page
    # query_results = occasion.objects.all()
    # query_results2 = Clothing.objects.all()
    # context = {'occasion':query_results, 'Clothing': query_results2}

    # # generate packing list and add it to context
    # trip = Trip.objects.filter(trip_userID=request.user).latest('id')
    # packing_list = generate_packing_list(trip)

    # print(packing_list)

    # context['packing_list'] = packing_list

    return render(request, 'saved_trips.html')
