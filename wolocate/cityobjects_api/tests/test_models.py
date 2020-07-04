import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

class TestCityObjects:
    def test_init(self):
        obj_type = mixer.blend('cityobjects_api.CityObjectType')
        object_photo = mixer.blend('cityobjects_api.CityObjectPhoto')
        obj = mixer.blend('cityobjects_api.CityObject')
        assert obj.id == 1, 'Should init id to 1'
        assert type(obj.object_type) == type(obj_type), 'type should be a foreign key to table CityObjectType'
        assert type(obj.latitude) == float, 'Latitude should be a float value'
        assert type(obj.longitude) == float, 'Longitude should be a float value'

        assert type(obj.city) == str, 'City should be a string'
        assert type(obj.postal_code) == int, 'Postal code should be a string'

        assert type(obj.object_photo) == type(object_photo), 'object_photo should be a foreign key to CityObjectPhoto'


class TestCityObjectType:
    def test_init(self):
        obj = mixer.blend('cityobjects_api.CityObjectType')
        assert obj.id == 1, 'CityObjectType Should init id to 1'

class TestCityObjectsUser:
    def test_init(self):
        obj = mixer.blend('cityobjects_api.CityObjectsUser')
        assert obj.id == 1, 'CityObjectsUser Should init id to 1'