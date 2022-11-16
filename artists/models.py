from django.db import models
from django.db.models import Q, Count
from users.models import User


class ArtistManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(approved_albums=Count('albums', filter=Q(albums__is_approved=True)))


class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='artist')
    stage_name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    social_link = models.URLField(max_length=200, blank=True, null=False)
    objects = ArtistManager()


    class Meta:
        # This is the default ordering of the model
        ordering = ['stage_name']
        # This is the default table name of the model
        db_table = 'artists'


    def __str__(self):
        # This is the default string representation of the model
        return self.stage_name