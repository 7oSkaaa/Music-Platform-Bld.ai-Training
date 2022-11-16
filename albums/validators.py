from rest_framework.exceptions import ValidationError as SerializerValidationError
from django.forms import ValidationError as FormValidationError


def validate_albums_serializer(self):
    if self.songs.count() < 1:
        raise SerializerValidationError('Album must have at least one song')
    
def validate_albums_form(self, obj):
    if obj.songs.count() < 1:
        raise FormValidationError('Album must have at least one song')