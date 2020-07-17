from rest_framework import serializers
from .models import *


class CityObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityObject
        fields = '__all__'


class CityObjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityObjectType
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CityObjectPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CityObjectPhoto
        fields = '__all__'

    def get_image_path(self, city_photo_object):
        return "blah"

