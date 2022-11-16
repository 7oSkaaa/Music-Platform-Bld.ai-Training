from .models import User
from rest_framework import permissions
from .permissions import IsTheCurrentUser
from rest_framework import generics
from .serializers import UserSerializer

class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsTheCurrentUser]