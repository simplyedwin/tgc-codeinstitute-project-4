from django.db import models
import datetime
from products.models import Plant
from django.contrib.auth.models import User
from checkout.models import Order

# Create your models here.


class Review(models.Model):
    title = models.CharField(blank=False, max_length=255)
    content = models.TextField(blank=False)
    date = models.DateField(default=datetime.date.today)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    reviewed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=False)
    order = models.OneToOneField(Order, on_delete=models.CASCADE,
                                    primary_key=True,)

    def __str__(self):
        return self.title
