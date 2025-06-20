from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Menu

# Serializer for the Menu model
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

# Serializer for Django's built-in User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
