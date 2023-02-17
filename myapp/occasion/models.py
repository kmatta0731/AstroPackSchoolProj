# Create your models here.
from django.db import models
from django.conf import settings


class occasion(models.Model):
    occasion = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    occasion_item_category = models.ForeignKey('Item_Category', on_delete = models.CASCADE, null = True)
    occasion_gender = models.ForeignKey('Gender', on_delete = models.CASCADE, null = True) 


    def __str__(self):
        return self.occasion

class Essential(models.Model):
    Essentials = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    essentials_item_category = models.ForeignKey('Item_Category', on_delete = models.CASCADE, null = True)
    essentials_gender = models.ForeignKey('Gender', on_delete = models.CASCADE, null = True) 


    def __str__(self):
        return self.Essentials

class Comfort(models.Model):
    Comfort = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    comfort_item_category = models.ForeignKey('Item_Category', on_delete = models.CASCADE, null = True)
    comfort_gender = models.ForeignKey('Gender', on_delete = models.CASCADE, null = True) 

    def __str__(self):
        return self.Comfort

class Electronic(models.Model):
    Electronic = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    electronic_item_category = models.ForeignKey('Item_Category', on_delete = models.CASCADE, null = True)
    electronic_gender = models.ForeignKey('Gender', on_delete = models.CASCADE, null = True) 


    def __str__(self):
        return self.Electronic

class Toiletrie(models.Model):
    Toiletries = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    toiletries_item_category = models.ForeignKey('Item_Category', on_delete = models.CASCADE, null = True)
    toiletries_gender = models.ForeignKey('Gender', on_delete = models.CASCADE, null = True) 

    def __str__(self):
        return self.Toiletries

class Health(models.Model):
    Health = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    health_item_category = models.ForeignKey('Item_Category', on_delete = models.CASCADE, null = True)
    health_gender = models.ForeignKey('Gender', on_delete = models.CASCADE, null = True) 


    def __str__(self):
        return self.Health        

class Clothing(models.Model):
    Clothing = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    clothing_item_category = models.ForeignKey('Item_Category', on_delete = models.CASCADE, null = True)
    clothing_gender = models.ForeignKey('Gender', on_delete = models.CASCADE, null = True) 



    def __str__(self):
        return self.Clothing                

class Accessorie(models.Model):
    Accessories = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    accessories_item_category = models.ForeignKey('Item_Category', on_delete = models.CASCADE, null = True)
    accessories_gender = models.ForeignKey('Gender', on_delete = models.CASCADE, null = True) 

    def __str__(self):
        return self.Accessories      

class Shoe(models.Model):
    shoes = models.CharField(max_length=150)
    shoes_description = models.CharField(max_length=150)
    shoes_item_category = models.ForeignKey('Item_Category', on_delete = models.CASCADE, null = True) 
    shoes_gender = models.ForeignKey('Gender', on_delete = models.CASCADE, default = 'Male')


    def __str__(self):
        return self.shoes

class Item_Category(models.Model):
    description = models.CharField(max_length = 150)

    def __str__(self):
        return self.description

Gender_Choices = (
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other"),
)
class Gender(models.Model):
    gen = models.CharField(max_length = 1,choices = Gender_Choices,default = "M")
    #description = models.CharField(max_length = 150)
    def __str__(self):
        return self.gen

class Trip(models.Model): #Currently a dummy table
    trip_userID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, default = settings.AUTH_USER_MODEL )
    trip_item_category = models.ForeignKey('Item_Category', on_delete = models.CASCADE, null = True)
    trip_destination = models.CharField(max_length = 150)
    trip_start_date = models.CharField(max_length = 150)
    trip_end_date = models.CharField(max_length = 150)
    trip_occasion= models.ForeignKey('occasion', on_delete = models.CASCADE, null = True)
    trip_gender= models.ForeignKey('Gender', on_delete = models.CASCADE, null = True)
    trip_weather= models.CharField(max_length = 150)
    occasion = models.CharField(max_length=150)
    description = models.CharField(max_length=150)


    def __str__(self):
        return self.userID #Change this