from rest_framework import serializers
from rest_framework.serializers import ValidationError
from users.models import User

class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, required=True)
    email = serializers.EmailField(max_length=100, required=True)
    password1 = serializers.CharField(max_length=100, required=True)
    password2 = serializers.CharField(max_length=100, required=True)
    
    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email already exists')
        return email
    
    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username already exists')
        return username
    
    def validate_password(self, data):
        if not data.get('password1') or not data.get('password2'):
            raise ValidationError("Please enter a password and confirm it.")
        if data.get('password1') != data.get('password2'):
            raise ValidationError("Those passwords don't match.")
        return data

    def validate_password_strong(self, password1):
        if len(password1) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password1):
            raise ValidationError("Password must contain at least 1 digit.")
        if not any(char.isalpha() for char in password1):
            raise ValidationError("Password must contain at least 1 letter.")
        if not any(char.isupper() for char in password1):
            raise ValidationError("Password must contain at least 1 uppercase letter.")
        return password1