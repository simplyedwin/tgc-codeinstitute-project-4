from django.db import models
from django.contrib.auth.models import User
from products.models import Plant
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class UserInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    favourite_plant = models.ForeignKey(Plant, models.SET_NULL,
                                        blank=True,
                                        null=True)

    def __str__(self):
        return self.user


@receiver(post_save, sender=User)
def create_user_info(sender, instance, created, **kwargs):
    if created:
        UserInfo.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_info(sender, instance, **kwargs):
    instance.profile.save()
