from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class NewUser(User):
    discount = models.BooleanField(default=False)
    image = CloudinaryField('image')
    token = models.IntegerField(null=True, blank=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username