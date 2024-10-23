from django.db import models
from cloudinary.models import CloudinaryField
from store.models.product import Product
# Create your models here.

class Image(models.Model):
    image = CloudinaryField('image')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    