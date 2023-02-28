from occasion.models import *

def generate_packing_list(trip):
    destination = trip.trip_destination
    temp_range = trip.temp_range
    occasion = trip.occasion
    gender = trip.gender

    print(gender)
    print(temp_range)
    
    # Get the items based on occasion and gender
    clothing_items = Clothing.objects.filter(clothing_gender__gen=gender, clothing_temp=temp_range)
    accessory_items = Accessorie.objects.filter(accessories_gender__gen=gender)
    toiletry_items = Toiletrie.objects.filter(toiletries_gender__gen=gender)
    electronic_items = Electronic.objects.filter(electronic_gender__gen=gender)
    comfort_items = Comfort.objects.filter(comfort_gender__gen=gender)
    health_items = Health.objects.filter(health_gender__gen=gender)
    shoe_items = Shoe.objects.filter(shoes_gender__gen=gender, shoes_temperature=temp_range)
    
    print(clothing_items)
    # Create the packing list dictionary
    packing_list = {
        'Clothing': clothing_items,
        'Accessories': accessory_items,
        'Toiletries': toiletry_items,
        'Electronics': electronic_items,
        'Comfort': comfort_items,
        'Health': health_items,
        'Shoes': shoe_items
    }

    return packing_list
