from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.


class Plant(models.Model):
    name = models.CharField(blank=False, max_length=255)
    species = models.CharField(blank=False, max_length=255)
    size = models.CharField(blank=False, max_length=100)
    description = models.TextField(blank=False)
    rating = models.IntegerField(blank=False)
    watering = models.CharField(blank=False, max_length=100)
    sunlight = models.CharField(blank=False, max_length=100)
    level = models.CharField(blank=False, max_length=100)
    country = models.CharField(blank=False, max_length=100)
    image = ImageField(blank=True, manual_crop="")
    price = models.DecimalField(max_digits=10, decimal_places=3, blank=False)

    def __str__(self):
        return self.name
