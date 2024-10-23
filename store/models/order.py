from django.db import models
from django.contrib.auth.models import User
from django.core import validators

class Order(models.Model):
    quantity = models.IntegerField(validators=[validators.MinValueValidator(1)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
