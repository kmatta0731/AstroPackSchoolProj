from occasion.models import *
from django.db.models import Q


def generate_packing_list(trip):
    destination = trip.trip_destination
    temp_range = trip.temp_range
    occasion = trip.occasion
    gender = trip.gender
    activities = trip.activities

    print(gender)
    print(temp_range)

    for activity in trip.activities.all():
        print(activity.name)
    
    # Get the items based on occasion and gender
    clothing_items = Clothing.objects.filter(Q(clothing_gender__gen=gender) | Q(clothing_gender__gen='other'), Q(clothing_temp=temp_range) | Q(clothing_temp = 'Warm') )
    accessory_items = Accessorie.objects.filter(Q(accessories_gender__gen=gender) | Q(accessories_gender__gen='other'))
    toiletry_items = Toiletrie.objects.filter(Q(toiletries_gender__gen=gender) | Q(toiletries_gender__gen='other'))
    electronic_items = Electronic.objects.all()
    essential_items = Essential.objects.all()
    comfort_items = Comfort.objects.all()
    health_items = Health.objects.filter(Q(health_gender__gen=gender) | Q(health_gender__gen= 'other'))
    shoe_items = Shoe.objects.filter(Q(shoes_gender__gen=gender) | Q(shoes_gender__gen='other') & Q(shoes_activities = 'None') | Q(shoes_activities = activities)  , shoes_temperature=temp_range )
    
    included_items = []     
    for item in shoe_items:  # ------ filter out shoes that match activity user selected ----- #
            if not activities.filter(name__iexact=item.shoes_activities).exists():
                continue
            included_items.append(item)
            shoe_items = included_items

    #included_items2 = []     
    #for item in clothing_items:  # ------ filter out shoes that match activity user selected ----- #
     #   if not activities.filter(name__iexact=item.clothing_activity).exists():
      #      continue
       # included_items2.append(item)
    #clothing_items = included_items2
    
    # Create the packing list dictionary
    packing_list = {
        'Clothing': clothing_items,
        'Accessories': accessory_items,
        'Toiletries': toiletry_items,
        'Electronics': electronic_items,
        'Comfort': comfort_items,
        'Health': health_items,
        'Shoes': shoe_items,
        'Essentials': essential_items,
    }

    return packing_list
