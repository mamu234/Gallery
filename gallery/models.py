from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length =50)

class photos(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')