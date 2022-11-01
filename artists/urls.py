from django.urls import path
from .views import ArtistView, ArtistDetailView


urlpatterns = [
    path('', ArtistView.as_view()),
    path('<int:pk>/', ArtistDetailView.as_view()),
]