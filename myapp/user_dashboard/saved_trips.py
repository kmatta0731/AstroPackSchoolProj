from occasion.models import *

def generate_saved_trip(trip):
    
    tripName = trip.trip_destination

    for trip in trip.tripName.all():
        print(tripName)

    trip_list = {
        'UserID': tripName
    }

    return trip_list