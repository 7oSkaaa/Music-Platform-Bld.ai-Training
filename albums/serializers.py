from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Album


# validation for the serializer
def validate_albums(self):
    if self.songs.count() < 1:
        raise ValidationError('Album must have at least one song')


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = '__all__'
        validators = [validate_albums]