from django.db import models

from allauth.account.signals import user_signed_up
from django.contrib.auth.models import User
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    phone_numer = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.ImageField(max_length=300, null=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.user)

class test(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    test_acc = models.IntegerField(null=True )
    def __str__(self) -> str:
        return str(self.user)

@receiver(user_signed_up, sender=User)
def create_user_profile(sender, **kwargs):

    Profile.objects.create(
        user=kwargs['user']
    )
