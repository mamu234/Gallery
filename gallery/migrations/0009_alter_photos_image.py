# Generated by Django 4.0.5 on 2022-06-12 12:15

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
