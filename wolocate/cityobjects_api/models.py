from django.db import models
from .utils import UploadToPathAndRename


# Create your models here.
class CityObject(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    city = models.CharField(max_length=64)
    object_type = models.ForeignKey('CityObjectType', on_delete=models.CASCADE)
    postal_code = models.IntegerField()
    city_object_photo = models.ForeignKey('CityObjectPhoto', on_delete=models.CASCADE)


class CityObjectType(models.Model):
    object_type = models.CharField(max_length=64, unique=True)


class CityObjectPhoto(models.Model):
    upload_date = models.DateTimeField(auto_now_add=True)
    image_path = models.ImageField(upload_to=UploadToPathAndRename(""), max_length=124)
    contributing_user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)


class UserProfile(models.Model):
    email_sha256 = models.CharField(max_length=64)

