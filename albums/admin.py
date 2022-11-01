from django.contrib import admin
from .models import Album
from .forms import AlbumForm


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ['creation_date']
    list_display = ('name', 'artist', 'creation_date', 'release_date' ,'cost', 'is_approved')
    fields = ['name', 'artist', 'creation_date', 'release_date', 'cost', 'is_approved']
    

# register the model with the admin site
admin.site.register(Album, AlbumAdmin, form=AlbumForm)