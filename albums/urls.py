from django.urls import path
from .views import AlbumView, AlbumFilterView

urlpatterns = [
    path('', AlbumView.as_view()),
    path('filter/', AlbumFilterView.as_view())
]