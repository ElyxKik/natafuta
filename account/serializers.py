# serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import AgentUser

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentUser
        fields = ('id', 'username', 'email', 'is_admin')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = AgentUser(
            username=validated_data['username'],
            email=validated_data['email'],
            is_admin=validated_data.get('is_admin', False),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
