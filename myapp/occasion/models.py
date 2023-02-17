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
    shoes_description = models.CharField(max_length=150)
    shoes_item_category = models.ForeignKey('Item_Category', on_delete = models.CASCADE, null = True) #Null = true so default is empty choice
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