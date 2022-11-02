from rest_framework import serializers
from rest_framework.serializers import ValidationError
from users.models import User

def validate_email(email):
    if User.objects.filter(email=email).exists():
        raise ValidationError('Email already exists')
    return email

def validate_username(username):
    if User.objects.filter(username=username).exists():
        raise ValidationError('Username already exists')
    return username

def validate_password(self):
    if not self['password'] or not self['confirm_password']:
        raise ValidationError("Please enter a password and confirm it.")
    if self['password'] != self['confirm_password']:
        raise ValidationError("The passwords do not match")
    return self['password']

def validate_password_strong(password):
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    if not any(char.isdigit() for char in password):
        raise ValidationError("Password must contain at least 1 digit.")
    if not any(char.isalpha() for char in password):
        raise ValidationError("Password must contain at least 1 letter.")
    if not any(char.isupper() for char in password):
        raise ValidationError("Password must contain at least 1 uppercase letter.")
    return password

class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, required=True, validators = [validate_username])
    email = serializers.EmailField(max_length=100, required=True, validators = [validate_email])
    password = serializers.CharField(max_length=100, required=True, validators = [validate_password_strong], style = {'input_type': 'password'})
    confirm_password = serializers.CharField(max_length=100, required=True, validators = [validate_password_strong], style = {'input_type': 'password'})
    bio = serializers.CharField(max_length=256, required=False)
    

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio')
        validators = [validate_password]