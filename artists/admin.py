from django.contrib import admin
from albums.models import Album
from .models import Artist


# Allow the admin to create albums for the artist from from the artist's editing form
class AlbumInline(admin.TabularInline):
    model = Album
    extra =  0


class ArtistAdmin(admin.ModelAdmin):    
    field = ('stage_name', 'social_link', 'approved_albums')
    list_display = ('stage_name', 'social_link', 'approved_albums')
    inlines = [AlbumInline]
     
    
    # count the number of approved albums for each artist
    def approved_albums(self, Artist):
        return Artist.albums.filter(is_approved=True).count()
    

# register the model with the admin site
admin.site.register(Artist, ArtistAdmin)