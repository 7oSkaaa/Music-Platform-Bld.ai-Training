from django.urls import path
from views import UserView

user_detail = UserView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
}) 

urlpatterns = [
    path('<int:pk>/', user_detail, name= "user detail"),
]
