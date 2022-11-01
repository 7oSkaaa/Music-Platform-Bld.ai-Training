from django.db import models
from django.db.models import Q, Count


class ArtistManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(approved_albums=Count('album', filter=Q(album__is_approved=True)))


class Artist(models.Model):
    stage_name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    social_link = models.URLField(max_length=200, blank=True, null=False)
    objects = ArtistManager()


    class Meta:
        # This is the default ordering of the model
        ordering = ['stage_name']


    def __str__(self):
        # This is the default string representation of the model
        return self.stage_name