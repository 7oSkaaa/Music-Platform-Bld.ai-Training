from django.db import models
from imagekit.models import ImageSpecField
from django.core.validators import FileExtensionValidator
from model_utils.models import TimeStampedModel
from artists.models import Artist

class AlbumManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_approved=True)

class Album(TimeStampedModel):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=False, related_name='albums')
    name = models.CharField(default='New Album', max_length=100, blank=True)
    release_date = models.DateTimeField(null=False, blank=False)
    cost = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False)
    is_approved = models.BooleanField(default = False) 
    objects = AlbumManager()
    
    
    def __str__(self):
        # This is the default string representation of the model
        return self.name
    
    
    class Meta:
        # This is the default table name of the model
        db_table = 'albums'
        # This is the validation of the model
    
        
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, default=album.name)
    image = models.ImageField(upload_to='static/images')
    image_thumbnail = ImageSpecField(source='image', format='JPEG')
    audio = models.FileField(upload_to='static/audio', null=True,validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])


    def __str__(self):
        return self.name


    class Meta:
        # This is the default table name of the model
        db_table = 'songs'
