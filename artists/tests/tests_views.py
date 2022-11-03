from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from ..models import Artist
import pytest


class ArtistViewTest(TestCase):
    def setUp(self):
        self.endpoints = '/artists/'
        self.artist = {
            "stage_name" : "Ahmed Hossam",
            "social_link" : "https://www.facebook.com/ahmed.hossam.581"
        }
    
    def test_create_artist_success(self):
        # test create artist with valid data
        response = self.client.post(f'{self.endpoints}', self.artist)
        assert response.status_code == status.HTTP_201_CREATED
        
    
    def test_create_artist_fail(self):
        # test create artist with empty data
        response = self.client.post(f'{self.endpoints}', {})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
        # test create artist with already existing stage_name
        response = self.client.post(f'{self.endpoints}', self.artist)
        response = self.client.post(f'{self.endpoints}', self.artist)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
   
        
    def  test_get_artist_fail(self):
        # test get artist with invalid id
        response = self.client.get(f'{self.endpoints}1/')
        assert response.status_code == status.HTTP_404_NOT_FOUND
    
    
    def test_get_artist_success(self):
        # test get artist with valid id
        response = self.client.post(f'{self.endpoints}', self.artist)
        assert response.status_code == status.HTTP_201_CREATED
        response = self.client.get(f'{self.endpoints}1/')
        assert response.status_code == status.HTTP_200_OK
        
    
    def test_update_artist_success(self):
        # test update artist with valid data
        
        # create artist first
        response = self.client.post(f'{self.endpoints}', self.artist)
        assert response.status_code == status.HTTP_201_CREATED
        
        # update artist that created before
        self.artist["stage_name"] = "7oSkaa"
        response = self.client.put(f'{self.endpoints}1/', self.artist, kwargs={'pk': 1}, content_type='application/json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data["stage_name"] == "7oSkaa"
        
        
    def test_update_artist_failed(self):
        # test update artist with valid data
        
        # test update artist with invalid id
        response = self.client.put(f'{self.endpoints}1/', self.artist, kwargs={'pk': 1}, content_type='application/json')
        assert response.status_code == status.HTTP_404_NOT_FOUND
        
        # create artist first
        response = self.client.post(f'{self.endpoints}', self.artist)
        assert response.status_code == status.HTTP_201_CREATED
        
        # update artist that created before
        self.artist["stage_name"] = "7oSkaa"
        response = self.client.put(f'{self.endpoints}1/', self.artist, kwargs={'pk': 1})
        assert response.status_code == status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
    
    
    def test_artist_delete_success(self):
        # test delete artist with valid id
        
        # create artist first
        response = self.client.post(f'{self.endpoints}', self.artist)
        assert response.status_code == status.HTTP_201_CREATED
        
        # delete artist that created before
        response = self.client.delete(f'{self.endpoints}1/')
        assert response.status_code == status.HTTP_200_OK
        
        # test get artist with deleted id
        response = self.client.get(f'{self.endpoints}1/')
        assert response.status_code == status.HTTP_404_NOT_FOUND
        
    
    def test_artist_delete_fail(self):
        # test delete artist with invalid id
        response = self.client.delete(f'{self.endpoints}1/')
        assert response.status_code == status.HTTP_404_NOT_FOUND