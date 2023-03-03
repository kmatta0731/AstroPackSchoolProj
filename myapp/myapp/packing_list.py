from occasion.models import *

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
    clothing_items = Clothing.objects.filter(clothing_gender__gen=gender, clothing_temp=temp_range)
    accessory_items = Accessorie.objects.filter(accessories_gender__gen=gender)
    toiletry_items = Toiletrie.objects.filter(toiletries_gender__gen=gender)
    electronic_items = Electronic.objects.all()
    essential_items = Essential.objects.all()
    comfort_items = Comfort.objects.filter(comfort_gender__gen=gender)
    health_items = Health.objects.filter(health_gender__gen=gender)
    shoe_items = Shoe.objects.filter(shoes_gender__gen=gender, shoes_temperature=temp_range)
    
    included_items = []     
    for item in shoe_items:  # ------ filter out shoes that match activity user selected ----- #
        if not activities.filter(name__iexact=item.shoes_activities).exists():
            continue
        included_items.append(item)
    shoe_items = included_items
    
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
