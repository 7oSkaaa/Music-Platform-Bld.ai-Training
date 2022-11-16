from rest_framework import status
from rest_framework.test import APIClient
import pytest


endpoint = '/authentication'


def validate_response(response, user):
    response_user = response.data['user']
    assert response_user['username'] == user['username']
    assert response_user['email'] == user['email']
    assert response_user['bio'] == user['bio']
    assert 'token' not in response_user
    assert 'token' in response.data
    assert 'id' in response_user
    assert 'password' not in response_user
    

@pytest.mark.django_db
def test_login_success(client):
    
    user = {
        'username' : "ahmed_7oSkaaa",
        'email' : "ahmed.7oskaa@gmail.com",
        'password' : "Password#1",
        'confirm_password' : "Password#1",
        "bio" : "I am a software engineer"
    }

    # register the user
    response = client.post(f'{endpoint}/register/', user)
    assert response.status_code == status.HTTP_201_CREATED

    
    # login the user
    response = client.post(f'{endpoint}/login/', {'username' : "ahmed_7oSkaaa", 'password' : "Password#1",})
    assert response.status_code == status.HTTP_200_OK      
    validate_response(response, user)


@pytest.mark.django_db
def test_login_fail(client):
        
    # login the user
    response = client.post(f'{endpoint}/login/', {'username' : "ahmed_7oSka", 'password' : "Password#1",})
    assert response.status_code == status.HTTP_400_BAD_REQUEST