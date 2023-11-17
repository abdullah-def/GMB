from django.contrib import admin

# Register your models here.
from . models import StripeCustomer, Product


admin.site.register(StripeCustomer)
admin.site.register(Product)