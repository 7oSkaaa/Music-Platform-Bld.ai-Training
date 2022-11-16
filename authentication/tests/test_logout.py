from rest_framework import status
from rest_framework.test import APIClient
import pytest


endpoint = '/authentication'


@pytest.mark.django_db
def test_logout_success(auth_client):
    client = auth_client()
    response = client.post(f'{endpoint}/logout/')
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_logout_fail(client):
    response = client.post(f'{endpoint}/logout/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED