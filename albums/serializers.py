from rest_framework import serializers
from .models import Album, Song
from artists.models import Artist


class AlbumSerializer(serializers.ModelSerializer):

    name = serializers.CharField(default='New Album', max_length=100, required=False)
    artist = serializers.SerializerMethodField('_artist_data')
    cost = serializers.DecimalField(required=True, decimal_places=2, max_digits=10)
    release_date = serializers.DateTimeField(required=True)
    is_approved = serializers.BooleanField(default=False)
    
    class Meta:
        model = Album
        fields = ('id', 'artist', 'name', 'release_date', 'cost', 'is_approved')    

    def _artist_data(self, obj):
        return {
            "id": obj.artist.id,
            "stage_name": obj.artist.stage_name,
            "social_link": obj.artist.social_link
        }