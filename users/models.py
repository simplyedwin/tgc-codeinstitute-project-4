from django.db import models
from django.contrib.auth.models import User
from products.models import Plant
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

# to check for the age of the user


def age_check(value):
    today = date.today()
    age = relativedelta(today, value).years
    if value > today:
        raise ValidationError('Birthday cannot be in the future')
    elif(age < 6):
        raise ValidationError('Your age is below 6 years old')

# Create your models here.


class UserInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(
        null=True, blank=True, validators=[age_check])

    def __str__(self):
        return str(self.user)

# to create user information


@receiver(post_save, sender=User)
def create_user_info(sender, instance, created, **kwargs):
    if created:
        UserInfo.objects.create(user=instance)

# to save user information


@receiver(post_save, sender=User)
def save_user_info(sender, instance, **kwargs):
    instance.userinfo.save()
