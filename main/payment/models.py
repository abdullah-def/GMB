from django.contrib.auth.models import User
from django.db import models


class StripeCustomer(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    stripe_price =models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return str(self.name)