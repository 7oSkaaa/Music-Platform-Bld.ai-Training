from users.models import User
from artists.models import Artist
from ..models import Album
from ..serializers import AlbumSerializer
from datetime import datetime
from dateutil.parser import parse
from decimal import Decimal
import zoneinfo, pytest


@pytest.mark.django_db
def test_serializer_with_valid_data():
    
    # generate data for serializer
    serializer = AlbumSerializer(data={
        "name": "album",
        "release_date": datetime(2020, 10, 10, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
        "cost": 100
    })

    # test serializer is valid
    serializer.is_valid(raise_exception=False)
    assert not serializer.errors
    
    # test serializer data
    data = serializer.validated_data
    assert data["name"] == "album"
    assert data["release_date"] == datetime(2020, 10, 10, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')) 
    assert data["cost"] == 100
    

@pytest.mark.django_db
def test_serializer_with_missing_data():
    
    # test with missing cost
    serializer = AlbumSerializer(data={
        "name": "album",
        "release_date": datetime(2020, 10, 10, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
    })

    # test serializer is not valid
    serializer.is_valid(raise_exception=False)
    assert serializer.errors
    assert serializer.errors.keys() == set(['cost'])
    
    # test with missing release_date
    serializer = AlbumSerializer(data={
        "name": "album",
        "cost": 100
    })
    
    serializer.is_valid(raise_exception=False)
    assert serializer.errors
    assert serializer.errors.keys() == set(['release_date'])
    
    # test with missing name
    serializer = AlbumSerializer(data={
        "release_date": datetime(2020, 10, 10, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
        "cost": 100
    })
    
    serializer.is_valid(raise_exception=False)
    assert not serializer.errors
    
    
@pytest.mark.django_db
def test_serializer_with_wrong_data():
    # test with wrong cost as string
    serializer = AlbumSerializer(data={
        "name": "album",
        "release_date": datetime(2020, 10, 10, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
        "cost": "string"
    })

    # test serializer is not valid
    serializer.is_valid(raise_exception=False)
    assert serializer.errors
    assert serializer.errors.keys() == set(['cost'])
    
    
@pytest.mark.django_db
def test_serializer_returns_expected_fields_and_data():
    # create user, artist and album
    user = User.objects.create_user(username='user')
    artist = Artist.objects.create(user=user, stage_name='artist')
    album = Album.objects.create(artist=artist, name='album', release_date=datetime(2020, 10, 10, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')), cost=100.10)

    # test serializer returns expected fields
    serializer = AlbumSerializer(album)

    # test serializer returns expected data
    assert serializer.data['id'] == album.id
    assert serializer.data['artist']['id'] == artist.id
    assert serializer.data['artist']['stage_name'] == artist.stage_name
    assert serializer.data['artist']['social_link'] == artist.social_link
    assert serializer.data['name'] == album.name
    assert parse(serializer.data['release_date']) == album.release_date
    assert float(Decimal(serializer.data['cost'])) == float(Decimal(album.cost))