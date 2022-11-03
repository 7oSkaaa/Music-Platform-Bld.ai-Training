from rest_framework import status
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
import pytest


class RegisterationTest(TestCase):
    
    def setUp(self):
        self.endpoint = '/authentication/register/'
        self.user = {
            "username" : "ahmed_hossam",
            "email" : "ahmed.7oskaa@gmail.com",
            "password" : "Ahmed11_",
            "confirm_password" : "Ahmed11_",
            "bio" : "I am a software engineer"
        }
        self.client = APIClient()
    
    
    @pytest.mark.django_db
    def test_register_success(self):
        response = self.client.post(f'{self.endpoint}', self.user)
        assert response.status_code == status.HTTP_201_CREATED
    
    
    @pytest.mark.django_db
    def test_register_fail(self):
        # test register with empty data
        response = self.client.post(f'{self.endpoint}', {})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
        # test register with already registered email
        response = self.client.post(f'{self.endpoint}', self.user)
        response = self.client.post(f'{self.endpoint}', self.user)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
        # test register with password less than 8 characters
        self.user["password"] = self.user["confirm_password"] = "Ahmed"
        response = self.client.post(f'{self.endpoint}', self.user)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
        # test register with password not containing a uppercase letter
        self.user['password'] = self.user["confirm_password"] = "ahmed2001"
        response = self.client.post(f'{self.endpoint}', self.user)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
        # test register with password not containing a lowercase letter
        self.user['password'] = self.user["confirm_password"] = "AHMED2001"
        response = self.client.post(f'{self.endpoint}', self.user)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
        # test register with password not containing a number
        self.user['password'] = self.user["confirm_password"] = "AhmedAhmed"
        response = self.client.post(f'{self.endpoint}', self.user)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
        # test register with invalid email
        self.user['password'] = self.user["confirm_password"] = "Ahmed2001"
        self.user['email'] = "ahmed.7oskaa"
        response = self.client.post(f'{self.endpoint}', self.user)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        

def validate_response(response, user):
    response_user = response.data['user']
    assert response_user['username'] == user['username']
    assert response_user['email'] == user['email']
    assert response_user['bio'] == user['bio']
    assert 'token' not in response_user
    assert 'token' in response.data
    assert 'id' in response_user
    assert 'password' not in response_user
    

class LoginTest(TestCase):
        
    def setUp(self):
        self.endpoint = '/authentication'
        self.validator = validate_response
             
    
    @pytest.mark.django_db
    def test_login_success(self):
        
        user = {
            'username' : "ahmed_7oSkaaa",
            'email' : "ahmed.7oskaa@gmail.com",
            'password' : "Password#1",
            'confirm_password' : "Password#1",
            "bio" : "I am a software engineer"
        }

        # register the user
        response = self.client.post(f'{self.endpoint}/register/', user)
        assert response.status_code == status.HTTP_201_CREATED
    
        
        # login the user
        response = self.client.post(f'{self.endpoint}/login/', {'username' : "ahmed_7oSkaaa", 'password' : "Password#1",})
        assert response.status_code == status.HTTP_200_OK      
        self.validator(response, user)
    
    
    @pytest.mark.django_db
    def test_login_fail(self):
        # login the user
        response = self.client.post(f'{self.endpoint}/login/', {'username' : "ahmed_7oSka", 'password' : "Password#1",})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
        
class LogoutTest(TestCase):
        
    def setUp(self):
        self.endpoint = '/authentication'
        
    
    # @pytest.mark.usefixtures("auth_client")
    # def test_logout_success(self, auth_client):
    #     client = auth_client()
    #     response = client.post(f'/authentication/logout/')
    #     assert response.status_code == status.HTTP_204_NO_CONTENT


    @pytest.mark.django_db
    def test_logout_fail(self):
        client = APIClient()
        response = client.post(f'{self.endpoint}/logout/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED