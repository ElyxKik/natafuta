# serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import AgentUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentUser
        fields = ('id', 'username', 'email', 'is_admin')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
