from django.urls import path
from .views import UserView


urlpatterns = [
    path('<int:pk>/', UserView.as_view(), name= "user detail"),
]
