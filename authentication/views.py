from rest_framework import generics, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from knox.auth import AuthToken
from users.models import User
from users.serializers import UserSerializer
from .serializers import UserRegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        # register user
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # create user        
        model_serializer = UserSerializer(data=serializer.data)
        model_serializer.is_valid(raise_exception=True)
        
        # store data
        [username, email, password] = [model_serializer.data['username'], model_serializer.data['email'], model_serializer.data['password']]        
        
        # create user object
        user = User.objects.create_user(username=username, email=email, password=password)
        
        # create token
        token = AuthToken.objects.create(user)
        
        return Response({
            "token" : token,
            "user" : {
                "id" : user.id,
                "username" : user.username,
                "email" : user.email,
                "bio" : user.bio
            }
        }, status=status.HTTP_201_CREATED)
        
        
class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AuthTokenSerializer

    def create(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # validate user
        user = serializer.validated_data['user']
        
        # create token        
        token = AuthToken.objects.create(user)

        return Response({
            "token" : token,
            "user" : {
                "id" : user.id,
                "username" : user.username,
                "email" : user.email,
                "bio" : user.bio
            }
        }, status=status.HTTP_200_OK)
