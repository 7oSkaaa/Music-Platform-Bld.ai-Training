from django import forms
from django.forms import ModelForm, ValidationError
from .models import Album


# validation in the form for albums
def validate_albums(self, Album):
    if Album.songs.count() < 1:
        raise ValidationError('Album must have at least one song')


class AlbumForm(forms.ModelForm):
    
    class Meta:
        model = Album
        fields = ['name', 'artist', 'release_date', 'cost', 'is_approved']
        validators = [validate_albums]
        
        
    # display help text in the admin panel
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_approved'].help_text = 'Approve the album if its name is not explicit'
        