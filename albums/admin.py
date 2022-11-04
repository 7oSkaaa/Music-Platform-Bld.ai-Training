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
    

    # return album songs
    def album_songs(self, Album):
        return Album.songs.count()


class SongAdmin(admin.ModelAdmin):
    
    fields = ['name', 'album', 'image', 'audio']


# register the model with the admin site
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)