import pytest

from django.urls import reverse
from collections import OrderedDict
from wolocate.settings import MEDIA_ROOT

from model_bakery import baker


@pytest.mark.django_db
def test_get_cityobject_list_return_code_200(api_client):
   url = reverse('cityobject-list')
   response = api_client.get(url)
   assert response.status_code == 200


def test_get_cityobject_list_return_code_404(api_client):
   url = reverse('cityobject-list') + "/whatever"
   response = api_client.get(url)
   assert response.status_code == 404


@pytest.mark.django_db
def test_get_cityobjecttype_list_return_code_200(api_client):
    url = reverse('cityobjecttype-list')
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_cityobjecttype_validation(api_client):
    url = reverse('cityobjecttype-list')

    post_data = OrderedDict()
    post_data['object_type'] ='glass-recycling-containers'
    expected_response = OrderedDict()
    expected_response['id'] = 1
    expected_response['object_type'] = post_data['object_type']

    response = api_client.post(url, post_data)
    assert response.status_code == 201

    # test uniqueness of object_type column
    response = api_client.post(url, post_data)
    assert response.status_code == 400, "object_type column is a unique column."


# READ: https://djangostars.com/blog/django-pytest-testing/
# 4. Data Validation with Pytest Parametrizing
@pytest.mark.django_db
def test_add_city_object_validation(api_client):
    url = reverse('cityobject-list')
    post_data = OrderedDict()
    post_data['latitude'] = -89.383838
    post_data['longitude'] = 90.383838
    post_data['city'] = "Tumkur"
    post_data['postal_code'] = 572102

    post_data['object_type'] = baker.make('cityobjects_api.CityObjectType').pk
    post_data['city_object_photo'] = baker.make('cityobjects_api.CityObjectPhoto').pk

    response = api_client.post(url, post_data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_user_email_field_should_be_hashed(api_client):
    url = reverse('userprofile-list')


@pytest.mark.django_db
def test_add_city_object_photo_validation(api_client):
    url = reverse('cityobjectphoto-list')

    post_data = OrderedDict()
    post_data['city_object'] = baker.make('cityobjects_api.CityObject').pk

    from django.core.files import File
    from os.path import join, dirname, abspath, basename
    from os import remove

    post_data['image_path'] = File(open(join(dirname(abspath(__file__)), "media", "gplv3.png"), "rb"))
    post_data['contributing_user'] = baker.make('cityobjects_api.UserProfile').pk

    response = api_client.post(url, post_data)
    assert response.status_code == 201, "cityobjectphoto post request should return 201"

    assert len(basename(response.data.get("image_path").split(".")[0])) == 32, \
        "image_path generated file name should be an uuid4 string"

    # clean up.
    remove(join(MEDIA_ROOT, basename(response.data.get("image_path"))))

