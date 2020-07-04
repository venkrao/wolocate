from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CityObject(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    city = models.CharField(max_length=64)
    object_type = models.ForeignKey('CityObjectType', on_delete=models.CASCADE)
    postal_code = models.IntegerField()
    object_photo = models.ForeignKey('CityObjectPhoto', on_delete=models.CASCADE)


class CityObjectType(models.Model):
    object_type = models.CharField(max_length=64, unique=True)


class CityObjectPhoto(models.Model):
    object_type = models.CharField(max_length=64)
    upload_date = models.DateTimeField(auto_now_add=True)
    image_path = models.CharField(max_length=128)
    contributing_user = models.ForeignKey('CityObjectsUser', on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)


class CityObjectsUser(models.Model):
    email_sha256 = models.CharField(max_length=64)
