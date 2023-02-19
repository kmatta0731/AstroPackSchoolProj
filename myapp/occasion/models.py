# Create your models here.
from django.db import models


class occasion(models.Model):
    occasion = models.CharField(max_length=150)
    description = models.CharField(max_length=150)


    def __str__(self):
        return self.occasion

class Essential(models.Model):
    Essentials = models.CharField(max_length=150)
    description = models.CharField(max_length=150)


    def __str__(self):
        return self.Essentials

class Comfort(models.Model):
    Comfort = models.CharField(max_length=150)
    description = models.CharField(max_length=150)


    def __str__(self):
        return self.Comfort

class Electronic(models.Model):
    Electronic = models.CharField(max_length=150)
    description = models.CharField(max_length=150)


    def __str__(self):
        return self.Electronic

class Toiletrie(models.Model):
    Toiletries = models.CharField(max_length=150)
    description = models.CharField(max_length=150)


    def __str__(self):
        return self.Toiletries

class Health(models.Model):
    Health = models.CharField(max_length=150)
    description = models.CharField(max_length=150)


    def __str__(self):
        return self.Health        

class Clothing(models.Model):
    Clothing = models.CharField(max_length=150)
    description = models.CharField(max_length=150)


    def __str__(self):
        return self.Clothing                

class Accessorie(models.Model):
    Accessories = models.CharField(max_length=150)
    description = models.CharField(max_length=150)


    def __str__(self):
        return self.Accessories      

class Shoe(models.Model):
    shoes = models.CharField(max_length=150)
    description = models.CharField(max_length=150)


    def __str__(self):
        return self.shoes


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
        return self.description #Change this