from django.contrib import admin
from .models import Album, Song
from .forms import AlbumForm
from .validators import validate_albums_form

# create a song inline
class SongInLine(admin.TabularInline):
    model = Song
    extra = 1


class AlbumAdmin(admin.ModelAdmin):
    form = AlbumForm
    list_display = ('name', 'artist', 'release_date' ,'cost', 'is_approved', 'album_songs')
    fields = ['name', 'artist', 'release_date', 'cost', 'is_approved']
    inlines = [SongInLine]
    
    
    # return exception if album has no songs
    def save_model(self, request, obj, form, change):
        validate_albums_form(self, obj)
        super().save_model(request, obj, form, change)


    # return album songs
    def album_songs(self, Album):
        return Album.songs.count()


class SongAdmin(admin.ModelAdmin):
    
    fields = ['name', 'album', 'image', 'image_thumbnail', 'audio']


# register the model with the admin site
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song)