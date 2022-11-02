from rest_framework import serializers
from .validators import validate_albums_serializer
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = '__all__'
        validators = [validate_albums_serializer]