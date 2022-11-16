from django.urls import path
from .views import ArtistView, ArtistDetailView
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)


urlpatterns = [
    path('', ArtistView.as_view()),
    path('<int:pk>/', ArtistDetailView.as_view()),
]

urlpatterns += router.urls