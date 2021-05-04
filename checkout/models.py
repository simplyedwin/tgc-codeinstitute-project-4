from django.db import models
from django.contrib.auth.models import User
from products.models import Plant
import datetime

# Create your models here.


class Order(models.Model):

    title = models.CharField(blank=True, max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=3, blank=False)
    datetime_ordered = models.DateField(default=datetime.date.today)
    plant = models.ForeignKey(
        Plant, on_delete=models.CASCADE, blank=True, null=True)
    order_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title + " " + str(self.datetime_ordered)
