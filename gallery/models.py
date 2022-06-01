from unicodedata import category
from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length =50)

def __str__(self):
    return self.name

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length =50)
    post = models.TextField()
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)