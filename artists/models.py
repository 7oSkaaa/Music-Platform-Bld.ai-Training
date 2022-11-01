from django.db import models


class Artist(models.Model):
    stageName = models.CharField(max_length=100, unique=True, blank=False, null=False)
    socialLink = models.URLField(max_length=200, blank=True, null=False)
    
    class Meta:
        # This is the default ordering for the model
        ordering = ['stageName']
        
        
    def __str__(self):
        # This is the default string representation of the model
        return self.stageName