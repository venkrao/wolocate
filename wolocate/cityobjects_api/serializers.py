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
