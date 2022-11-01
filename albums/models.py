from django.db import models
from artists.models import Artist


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=False, related_name='albums')
    name = models.CharField(default='New Album', max_length=100, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    release_date = models.DateTimeField(null=False, blank=False)
    cost = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False)
    is_approved = models.BooleanField(default = False) 
    
    
    def __str__(self):
        # This is the default string representation of the model
        return self.name