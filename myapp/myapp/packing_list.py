from occasion.models import *
from django.db.models import Q

copy_list2 = None

def generate_packing_list(trip):
    destination = trip.trip_destination
    temp_range = trip.temp_range
    occasion = trip.occasion
    gender = trip.gender
    activities = trip.activities.all()  ## this is what was causing iteration problem -- needed to include .all()

    # Get the items based on occasion and gender
    clothing_items = Clothing.objects.filter(Q(clothing_gender__gen=gender) | Q(clothing_gender__gen='other'), clothing_occasion=occasion, clothing_temp=temp_range, clothing_activity__in=activities).distinct()
    accessory_items = Accessorie.objects.filter(Q(accessories_gender__gen=gender) | Q(accessories_gender__gen='other'))
    toiletry_items = Toiletrie.objects.filter(Q(toiletries_gender__gen=gender) | Q(toiletries_gender__gen='other'))
    electronic_items = Electronic.objects.all()
    essential_items = Essential.objects.all()
    comfort_items = Comfort.objects.all()
    health_items = Health.objects.filter(Q(health_gender__gen=gender) | Q(health_gender__gen= 'other'))
    shoe_items = Shoe.objects.filter(Q(shoes_gender__gen=gender) | Q(shoes_gender__gen='other'), shoes_occasion=occasion, shoes_temperature=temp_range, shoes_activities__in=activities).distinct()
    equipment_items = Equipment.objects.filter(equipment_occasion=occasion, equipment_activity__in=activities).distinct()

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
        'Equipment': equipment_items,
    }

    copy_list = Generated_list (
        gen_tripID = trip,
        gen_qty_of_clothing = trip.length_of_trip
    )

    copy_list.save()

    clothingLoop(clothing_items, copy_list)
    comfortLoop(comfort_items, copy_list)
    electronicLoop(electronic_items, copy_list)
    essentialsLoop(essential_items, copy_list)
    healthLoop(health_items, copy_list)
    shoeLoop(shoe_items, copy_list)
    toiletriesLoop(toiletry_items, copy_list)
    accessoryLoop(accessory_items, copy_list)
    equipmentLoop(equipment_items, copy_list)

    # setcopyList(copy_list)

    return packing_list

# def setcopyList(copy_list):
#     global copy_list2  # define copy_list2 as global variable
#     copy_list2 = copy_list

# def getcopyList():
#     global copy_list2  # define copy_list2 as global variable
#     return copy_list2


def clothingLoop(clothing_items, copy_list):
    copy_list.gen_clothing.add(*clothing_items)

def comfortLoop(comfort_items, copy_list):
    copy_list.gen_comfort.add(*comfort_items)

def electronicLoop(electronic_items, copy_list):
    copy_list.gen_electronic.add(*electronic_items)

def essentialsLoop(essential_items, copy_list):
    copy_list.gen_essentials.add(*essential_items)

def healthLoop(health_items, copy_list):
    copy_list.gen_health.add(*health_items)

def shoeLoop(shoe_items, copy_list):
    copy_list.gen_shoe.add(*shoe_items)

def toiletriesLoop(toiletry_items, copy_list):
    copy_list.gen_toiletries.add(*toiletry_items)

def accessoryLoop(accessory_items, copy_list):
    copy_list.gen_accessories.add(*accessory_items)

def equipmentLoop(equipment_items, copy_list):
    copy_list.gen_equipment.add(*equipment_items)