from django.db import models 
from django.contrib.auth.models import User

from django.utils import timezone


class Image(models.Model):
 user = models.OneToOneField(User,on_delete=models.CASCADE)
 first_name = models.CharField(max_length=15)
 description = models.TextField()
 date_joined = models.DateTimeField(auto_now_add=timezone)
