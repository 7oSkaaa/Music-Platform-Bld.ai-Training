from django.contrib import admin
from .models import Artist

class ArtistAdmin(admin.ModelAdmin):    
    field = ('stage_name', 'social_link', 'approved_albums')
    list_display = ('stage_name', 'social_link', 'approved_albums')
    
    
    # count the number of approved albums for each artist
    def approved_albums(self, Artist):
        return Artist.albums.filter(is_approved=True).count()
    

# register the model with the admin site
admin.site.register(Artist, ArtistAdmin)