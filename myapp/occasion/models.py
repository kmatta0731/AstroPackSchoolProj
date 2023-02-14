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
    electronics = models.CharField(max_length=150)
    description = models.CharField(max_length=150)


    def __str__(self):
        return self.Electronics

class Toiletrie(models.Model):
    Toiletries = models.CharField(max_length=150)
    description = models.CharField(max_length=150)


    def __str__(self):
        return self.occasion

class Health(models.Model):
    Health = models.CharField(max_length=150)
    description = models.CharField(max_length=150)


    def __str__(self):
        return self.occasion        

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