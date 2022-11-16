import pytest, zoneinfo
from ..models import Album
from datetime import datetime
from users.models import User
from artists.models import Artist
from rest_framework import status
from dateutil.parser import parse
from decimal import Decimal


@pytest.mark.django_db
def test_post_success(auth_client):
    
    user = User.objects.create_user(username = 'user')
    artist = Artist.objects.create(user = user, stage_name = 'artist')
    client = auth_client(user)
    
    # test create album with valid data
    
    album = {
        "name" : "album",
        "release_date": datetime(2020, 10, 10, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
        "cost" : 100,
        "is_approved" : True,
    }
 
    response = client.post('/albums/', album)
    assert response.status_code == status.HTTP_201_CREATED
    
    data = response.data
    
    assert response.status_code == status.HTTP_201_CREATED
    assert data["name"] == "album"
    assert parse(data["release_date"]) == datetime(2020, 10, 10, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC'))
    assert float(Decimal(data["cost"])) == float(Decimal(100))
    assert data["is_approved"] == True
    assert data["artist"]["id"] == artist.id
    assert data["artist"]["stage_name"] == artist.stage_name
    assert data["artist"]["social_link"] == artist.social_link
 

@pytest.mark.django_db
def test_post_failed(client):
 
    # test create album with valid data but not authorized
    
    album = {
        "name" : "album",
        "release_date": datetime(2020, 10, 10, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
        "cost" : 100,
        "is_approved" : True,
    }
    
    response = client.post('/albums/', album)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_filter_success(auth_client):

    user = User.objects.create_user(username='user')
    artist = Artist.objects.create(user=user, stage_name='artist')
    client = auth_client(user)

    # create 3 albums

    album1 = {
        "name" : "album",
        "release_date": datetime(2020, 10, 10, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
        "cost" : 1000,
        "is_approved" : True,
    }

    album2 = {
        "name" : "album2",
        "release_date": datetime(2020, 10, 10, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
        "cost" : 2000,
        "is_approved" : True,   
    }
    
    album3 = {
        "name" : "album3",
        "release_date": datetime(2020, 10, 10, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
        "cost" : 3000,
        "is_approved" : True,
    }

    # create 3 albums
    album1_response = client.post('/albums/', album1)
    album2_response = client.post('/albums/', album2)
    album3_response = client.post('/albums/', album3)
    assert album1_response.status_code == status.HTTP_201_CREATED
    assert album2_response.status_code == status.HTTP_201_CREATED
    assert album3_response.status_code == status.HTTP_201_CREATED

    # test filter by cost less than 2000
    filtered_albums = client.get('/albums/?cost__lte=2000')
    assert filtered_albums.status_code == status.HTTP_200_OK
    filtered_albums = (filtered_albums.data["results"])
    filtered_albums_serialized = Album.objects.filter(cost__lte=2000).values()
    assert len(filtered_albums_serialized.values()) == len(filtered_albums) 
    
    # test filter by cost greater than 2000
    filtered_albums = client.get('/albums/?cost__gte=1000')
    assert filtered_albums.status_code == status.HTTP_200_OK
    filtered_albums = (filtered_albums.data["results"])
    filtered_albums_serialized = Album.objects.filter(cost__gte=1000).values()
    assert len(filtered_albums_serialized.values()) == len(filtered_albums) 
    
    
@pytest.mark.django_db
def test_filter_manual_success(auth_client):

    user = User.objects.create_user(username='user')
    artist = Artist.objects.create(user=user, stage_name='artist')
    client = auth_client(user)

    # create 3 albums

    album1 = {
        "name" : "album",
        "release_date": datetime(2020, 10, 10, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
        "cost" : 1000,
        "is_approved" : True,
    }

    album2 = {
        "name" : "album2",
        "release_date": datetime(2020, 10, 10, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
        "cost" : 2000,
        "is_approved" : True,   
    }
    
    album3 = {
        "name" : "album3",
        "release_date": datetime(2020, 10, 10, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
        "cost" : 3000,
        "is_approved" : True,
    }

    # create 3 albums
    album1_response = client.post('/albums/', album1)
    album2_response = client.post('/albums/', album2)
    album3_response = client.post('/albums/', album3)
    assert album1_response.status_code == status.HTTP_201_CREATED
    assert album2_response.status_code == status.HTTP_201_CREATED
    assert album3_response.status_code == status.HTTP_201_CREATED

    # test filter by cost less than 2000
    filtered_albums = client.get('/albums/filter/?cost__lte=2000')
    assert filtered_albums.status_code == status.HTTP_200_OK
    filtered_albums_serialized = Album.objects.filter(cost__lte=2000).values()
    assert len(filtered_albums_serialized.values()) == len(filtered_albums.data) 
    
    # test filter by cost greater than 2000
    filtered_albums = client.get('/albums/filter/?cost__gte=1000')
    assert filtered_albums.status_code == status.HTTP_200_OK
    filtered_albums_serialized = Album.objects.filter(cost__gte=1000).values()
    assert len(filtered_albums_serialized.values()) == len(filtered_albums.data)