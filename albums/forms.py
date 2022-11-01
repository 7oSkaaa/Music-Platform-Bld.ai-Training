from django import forms
from django.forms import ModelForm
from .models import Album
from .validators import validate_albums_form


class AlbumForm(forms.ModelForm):
    
    class Meta:
        model = Album
        fields = ['name', 'artist', 'release_date', 'cost', 'is_approved']
        validators = [validate_albums_form]
        
        
    # display help text in the admin panel
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_approved'].help_text = 'Approve the album if its name is not explicit'
        