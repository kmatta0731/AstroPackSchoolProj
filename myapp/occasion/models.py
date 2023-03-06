# Create your models here.
from django.db import models
from django.conf import settings

class Activities(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
    
class Occasion(models.Model):
    occasion = models.CharField(max_length=150)
    
    def __str__(self):
        return self.occasion
    
class TempRange(models.Model):
    temp = models.CharField(max_length=150)
    
    def __str__(self):
        return self.temp

class Essential(models.Model):
    Essentials = models.CharField(max_length=150)

    def __str__(self):
        return self.Essentials

class Comfort(models.Model):
    Comfort = models.CharField(max_length=150)

    def __str__(self):
        return self.Comfort

class Electronic(models.Model):
    Electronic = models.CharField(max_length=150)

    def __str__(self):
        return self.Electronic

class Toiletrie(models.Model):
    Toiletries = models.CharField(max_length=150)
    toiletries_gender = models.ForeignKey('Gender', on_delete = models.CASCADE, default=3, null=True) 

    def __str__(self):
        return self.Toiletries

class Health(models.Model):
    Health = models.CharField(max_length=150)
    health_gender = models.ForeignKey('Gender', on_delete = models.CASCADE, default=3, blank=True) 

    def __str__(self):
        return self.Health      

class Clothing(models.Model):
    Clothing = models.CharField(max_length=150)
    clothing_gender = models.ForeignKey('Gender', on_delete = models.CASCADE, default=3, null=True) 
    clothing_temp = models.ManyToManyField(TempRange)
    clothing_activity = models.ManyToManyField(Activities)
    clothing_occasion = models.ManyToManyField(Occasion)

    def __str__(self):
        return self.Clothing                
    
class Equipment(models.Model):
    Equipment = models.CharField(max_length=150)
    # equipment_activity = models.ForeignKey('Activities', on_delete = models.CASCADE, null=True)
    equipment_activity = models.ManyToManyField(Activities)
    equipment_occasion = models.CharField(max_length=150, default='Leisure')

    def __str__(self):
        return self.Equipment                

class Accessorie(models.Model):
    Accessories = models.CharField(max_length=150)
    accessories_gender = models.ForeignKey('Gender', on_delete = models.CASCADE, default=3, null=True) 

    def __str__(self):
        return self.Accessories     

class Shoe(models.Model):
    shoes = models.CharField(max_length=150)
    shoes_gender = models.ForeignKey('Gender', on_delete = models.CASCADE, default=3, null=True)
    shoes_temperature = models.ManyToManyField(TempRange)
    # shoes_activities = models.CharField(max_length=150, default='')
    shoes_activities = models.ManyToManyField(Activities)
    shoes_occasion = models.ManyToManyField(Occasion)
    
    def __str__(self):
        return self.shoes
    
Gender_Choices = (
    ("male", "male"),
    ("female", "female"),
    ("other", "other"),
)

class Gender(models.Model):
    gen = models.CharField(max_length = 150,choices = Gender_Choices, null=True)

    def __str__(self):
        return self.gen

class Trip(models.Model):
    trip_userID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, default = settings.AUTH_USER_MODEL )
    trip_destination = models.CharField(max_length = 150)
    trip_weather= models.CharField(max_length = 150)
    trip_start_date = models.CharField(max_length = 150)
    trip_end_date = models.CharField(max_length = 150)
    occasion = models.CharField(max_length=150)
    gender = models.CharField(max_length=150)
    length_of_trip = models.IntegerField()
    temp_range = models.CharField(max_length=150)
    activities = models.ManyToManyField(Activities) # using ManyToManyField
    
    def __str__(self):
        return self.trip_userID.username

class Generated_list(models.Model):
    gen_tripID = models.ForeignKey(Trip, on_delete = models.CASCADE, null = True)
    gen_accessories = models.ManyToManyField(Accessorie)
    gen_clothing = models.ManyToManyField(Clothing)    
    gen_qty_of_clothing = models.CharField(max_length=150) # Change this later
    gen_comfort = models.ManyToManyField(Comfort)
    gen_electronic = models.ManyToManyField(Electronic)
    gen_essentials = models.ManyToManyField(Essential)
    gen_health = models.ManyToManyField(Health)
    gen_shoe = models.ManyToManyField(Shoe)
    gen_toiletries = models.ManyToManyField(Toiletrie)
    gen_equipment = models.ManyToManyField(Equipment)

    def __str__(self):
        return 'Packing List for Trip: {}'.format(self.gen_tripID.trip_destination)