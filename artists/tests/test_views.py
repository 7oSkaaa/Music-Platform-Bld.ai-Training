from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from ..models import Artist
import pytest


@pytest.mark.django_db
def test_create_artist_success(client):
    
    endpoint = '/artists/'
    artist = {
        "stage_name" : "Ahmed Hossam",
        "social_link" : "https://www.facebook.com/ahmed.hossam.581"
    }
    
    # test create artist with valid data
    response = client.post(f'{endpoint}', artist)
    assert response.status_code == status.HTTP_201_CREATED
        
        
@pytest.mark.django_db
def test_create_artist_fail(client):
    
    endpoint = '/artists/'
    artist = {
        "stage_name" : "Ahmed Hossam",
        "social_link" : "https://www.facebook.com/ahmed.hossam.581"
    }
    
    # test create artist with empty data
    response = client.post(f'{endpoint}', {})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    # test create artist with already existing stage_name
    response = client.post(f'{endpoint}', artist)
    response = client.post(f'{endpoint}', artist)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def  test_get_artist_fail(client):
    
    endpoint = '/artists/'
    
    # test get artist with invalid id
    response = client.get(f'{endpoint}1/')
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_get_artist_success(client):
    
    endpoint = '/artists/'
    artist = {
        "stage_name" : "Ahmed Hossam",
        "social_link" : "https://www.facebook.com/ahmed.hossam.581"
    }
    
    # test get artist with valid id
    response = client.post(f'{endpoint}', artist)
    assert response.status_code == status.HTTP_201_CREATED
    response = client.get(f'{endpoint}1/')
    assert response.status_code == status.HTTP_200_OK
    

@pytest.mark.django_db
def test_update_artist_success(client):
    # test update artist with valid data
    
    endpoint = '/artists/'
    artist = {
        "stage_name" : "Ahmed Hossam",
        "social_link" : "https://www.facebook.com/ahmed.hossam.581"
    }
    
    # create artist first
    response = client.post(f'{endpoint}', artist)
    assert response.status_code == status.HTTP_201_CREATED
    
    # update artist that created before
    artist["stage_name"] = "7oSkaa"
    response = client.put(f'{endpoint}1/', artist, kwargs={'pk': 1})
    assert response.status_code == status.HTTP_200_OK
    assert response.data["stage_name"] == "7oSkaa"
    

@pytest.mark.django_db
def test_update_artist_failed(client):
    # test update artist with valid data
    
    endpoint = '/artists/'
    artist = {
        "stage_name" : "Ahmed Hossam",
        "social_link" : "https://www.facebook.com/ahmed.hossam.581"
    }
    
    # test update artist with invalid id
    response = client.put(f'{endpoint}1/', artist, kwargs={'pk': 1}, content_type='application/json')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    
    # create artist first
    response = client.post(f'{endpoint}', artist)
    assert response.status_code == status.HTTP_201_CREATED
    
    # update artist that created before
    artist["stage_name"] = "7oSkaa"
    response = client.put(f'{endpoint}/', artist)
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_artist_delete_success(client):
    # test delete artist with valid id
    
    endpoint = '/artists/'
    artist = {
        "stage_name" : "Ahmed Hossam",
        "social_link" : "https://www.facebook.com/ahmed.hossam.581"
    }
    
    # create artist first
    response = client.post(f'{endpoint}', artist)
    assert response.status_code == status.HTTP_201_CREATED
    
    # delete artist that created before
    response = client.delete(f'{endpoint}1/')
    assert response.status_code == status.HTTP_200_OK
    
    # test get artist with deleted id
    response = client.get(f'{endpoint}1/')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    

@pytest.mark.django_db
def test_artist_delete_fail(client):
    
    endpoint = '/artists/'
    
    # test delete artist with invalid id
    response = client.delete(f'{endpoint}1/')
    assert response.status_code == status.HTTP_404_NOT_FOUND