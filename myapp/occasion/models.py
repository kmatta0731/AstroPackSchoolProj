# Create your models here.
from django.db import models
from django.conf import settings

class Activities(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class Essential(models.Model):
    Essentials = models.CharField(max_length=150)

    def __str__(self):
        return self.Essentials

class Comfort(models.Model):
    Comfort = models.CharField(max_length=150)
    clothing_temp = models.CharField(max_length=150, default='')
    comfort_gender = models.ForeignKey('Gender', on_delete = models.CASCADE, default=3, null=True) 

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
    clothing_temp = models.CharField(max_length=150, default='')
    clothing_activity = models.ForeignKey('Activities', on_delete = models.CASCADE, null=True)
    clothing_occasion = models.CharField(max_length=150, default='Leisure')

    def __str__(self):
        return self.Clothing                
    
class Equipment(models.Model):
    Equipment = models.CharField(max_length=150)
    clothing_temp = models.CharField(max_length=150, default='')
    clothing_activity = models.ForeignKey('Activities', on_delete = models.CASCADE, null=True)
    clothing_occasion = models.CharField(max_length=150, default='Leisure')

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
    shoes_temperature = models.CharField(max_length=10, default='Warm')
    shoes_activities = models.CharField(max_length=150, default='')
    shoes_occasion = models.CharField(max_length=150, default='Leisure')

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
    temp_range = models.CharField(max_length=150, default='')
    activities = models.ManyToManyField(Activities) # using ManyToManyField

    def __str__(self):
        return self.trip_userID.username

class Generated_list(models.Model):
    gen_tripID = models.ForeignKey('Trip', on_delete = models.CASCADE, null = True)
    gen_accessories = models.ForeignKey('Accessorie', on_delete = models.CASCADE, null = True)
    gen_clothing = models.ForeignKey('Clothing', on_delete = models.CASCADE, null = True)
    gen_qty_of_clothing = models.CharField(max_length=150) # Change this later
    gen_comfort = models.ForeignKey('Comfort', on_delete = models.CASCADE, null = True)
    gen_electronic = models.ForeignKey('Electronic', on_delete = models.CASCADE, null = True)
    gen_essentials = models.ForeignKey('Essential', on_delete = models.CASCADE, null = True)
    gen_health = models.ForeignKey('Health', on_delete = models.CASCADE, null = True)
    gen_shoe = models.ForeignKey('Shoe', on_delete = models.CASCADE, null = True)
    gen_toiletries = models.ForeignKey('Toiletrie', on_delete = models.CASCADE, null = True)
    gen_gender = models.ForeignKey('Gender', on_delete = models.CASCADE, null = True)
    gen_weather = models.CharField(max_length=150) #Change this later

    def __str__(self):
        return self.gen_tripID #change this later

