from django.db import models
from django.core import validators


class Cart(models.Model):
    quantity = models.IntegerField(
        validators=[validators.MinValueValidator(1)])
