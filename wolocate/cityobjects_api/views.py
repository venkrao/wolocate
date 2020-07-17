from rest_framework import viewsets
from .models import *
from .serializers import *


class CityObjectsView(viewsets.ModelViewSet):
    queryset = CityObject.objects.all()
    serializer_class = CityObjectSerializer


class CityObjectTypeView(viewsets.ModelViewSet):
    queryset = CityObjectType.objects.all()
    serializer_class = CityObjectTypeSerializer


class UserProfileView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CityObjectPhotoView(viewsets.ModelViewSet):
    queryset = CityObjectPhoto.objects.all()
    serializer_class = CityObjectPhotoSerializer
