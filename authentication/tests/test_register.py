from rest_framework import status
from rest_framework.test import APIClient
import pytest


endpoint = '/authentication/register/'


@pytest.mark.django_db
def test_register_success(client):
    
    user = {
        "username" : "ahmed_hossam",
        "email" : "ahmed.7oskaa@gmail.com",
        "password" : "Ahmed11_",
        "confirm_password" : "Ahmed11_",
        "bio" : "I am a software engineer"
    }
    
    response = client.post(f'{endpoint}', user)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_register_fail(client):
    
    user = {
        "username" : "ahmed_hossam",
        "email" : "ahmed.7oskaa@gmail.com",
        "password" : "Ahmed11_",
        "confirm_password" : "Ahmed11_",
        "bio" : "I am a software engineer"
    }
    
    # test register with empty data
    response = client.post(f'{endpoint}', {})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    # test register with already registered email
    response = client.post(f'{endpoint}', user)
    response = client.post(f'{endpoint}', user)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    # test register with password less than 8 characters
    user["password"] = user["confirm_password"] = "Ahmed"
    response = client.post(f'{endpoint}', user)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    # test register with password not containing a uppercase letter
    user['password'] = user["confirm_password"] = "ahmed2001"
    response = client.post(f'{endpoint}', user)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    # test register with password not containing a lowercase letter
    user['password'] = user["confirm_password"] = "AHMED2001"
    response = client.post(f'{endpoint}', user)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    # test register with password not containing a number
    user['password'] = user["confirm_password"] = "AhmedAhmed"
    response = client.post(f'{endpoint}', user)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    # test register with invalid email
    user['password'] = user["confirm_password"] = "Ahmed2001"
    user['email'] = "ahmed.7oskaa"
    response = client.post(f'{endpoint}', user)
    assert response.status_code == status.HTTP_400_BAD_REQUEST