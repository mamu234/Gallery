from django.db import models
from cloudinary.models import CloudinaryField


class Photos(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('photo')
    
    
    def __str__(self):
        return self.title


class Category (models.Model):
    name = models.CharField(max_length =50)
    
    def __str__(self):
        return self.name

class Location (models.Model):
    name = models.CharField(max_length =50)
    
    def __str__(self):
        return self.name   