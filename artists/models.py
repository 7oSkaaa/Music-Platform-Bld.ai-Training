from django.db import models


class Artist(models.Model):
    stage_name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    social_link = models.URLField(max_length=200, blank=True, null=False)
    
    class Meta:
        # This is the default ordering for the model
        ordering = ['stage_name']
        
        
    def __str__(self):
        # This is the default string representation of the model
        return self.stage_name