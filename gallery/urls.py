from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


urlpatterns = [
path('', views.home, name='index'),
path('about', views.about, name='about'),
path(' category', views.category, name='category'),
path('location', views.location, name='location'),
path('upload/',views.upload,name='upload'),
path('update/<int:blog_id>',views.update,name='update'),
path('delete/<int:blog_id>',views.delete,name='delete'),
]


