from django.db import models
from django.contrib.auth.models import User
from store.models.cart import Cart
from store.models.order import Order
from django.core import validators

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=75)
    product_description = models.TextField(null=True, blank=True)
    price = models.CharField(max_length=12)
    quantity = models.IntegerField(validators=[validators.MinValueValidator(1)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ManyToManyField(Cart)
    order = models.ManyToManyField(Order)


    def __str__(self):
        return self.product_name