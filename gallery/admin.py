from django.contrib import admin
from .models import Category, Location, Photos

admin.site.register(Photos)
admin.site.register(Category)
admin.site.register(Location)

