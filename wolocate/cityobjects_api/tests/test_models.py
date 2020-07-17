import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db
import datetime
from model_bakery import baker


class TestCityObjects:
    def test_init(self):
        obj_type = mixer.blend('cityobjects_api.CityObjectType')

        obj = mixer.blend('cityobjects_api.CityObject')
        assert obj.id == 1, 'CityObjects Should init id to 1'
        assert type(obj.object_type) == type(obj_type), 'type should be a foreign key to table CityObjectType'
        assert type(obj.latitude) == float, 'Latitude should be a float value'
        assert type(obj.longitude) == float, 'Longitude should be a float value'

        assert type(obj.city) == str, 'City should be a string'
        assert type(obj.postal_code) == int, 'Postal code should be a string'


class TestCityObjectType:
    def test_init(self):
        obj = mixer.blend('cityobjects_api.CityObjectType')
        assert obj.id == 1, 'CityObjectType Should init id to 1'


class TestUserProfile:
    def test_init(self):
        obj = mixer.blend('cityobjects_api.UserProfile')
        assert obj.id == 1, 'UserProfile Should init id to 1'


class TestCityObjectPhoto:
    def test_init(self):
        obj = mixer.blend('cityobjects_api.CityObjectPhoto')
        contributing_user = baker.make('cityobjects_api.UserProfile')

        assert obj.id == 1, 'CityObjectPhoto Should init id to 1'
        assert isinstance(obj.upload_date, datetime.datetime), 'upload_date should be date time field'
        assert type(obj.contributing_user) == type(
            contributing_user), 'contributing_user should be foreign key to UserProfile'

        assert type(obj.approved) == bool, 'approved should be a boolean value'
