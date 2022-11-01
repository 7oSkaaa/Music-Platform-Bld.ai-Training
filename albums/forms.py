from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    
    class Meta:
        model = Album
        fields = ['name', 'artist', 'release_date', 'cost', 'is_approved']
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_approved'].help_text = 'Approve the album if its name is not explicit'