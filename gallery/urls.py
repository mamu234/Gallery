from django.urls import path
from .import views



urlpatterns = [
path('', views.index, name='index'),
path('about', views.about, name='about'),
path('category', views.category, name='category'),
path('location', views.location, name='location'),
]