from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('', views.index, name='index'),
path('about', views.about, name='about'),
path('upload/',views.upload,name='upload'),
path('update/<int:blog_id>',views.update,name='update'),
path('delete/<int:blog_id>',views.delete,name='delete'),
]


