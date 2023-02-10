# Create your models here.
from django.db import models


class occasion(models.Model):
    occasion = models.CharField(max_length=150)
    description = models.CharField(max_length=150)


    def __str__(self):
        return self.occasion
