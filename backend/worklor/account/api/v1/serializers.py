from rest_framework import serializers
from account.models import User
from user_profile.api.v1.serializers import UserProfileSerializer


class UserSerializer(serializers.ModelSerializer):
    joining_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)

    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'joining_date', 'updated_at', 'profile']
        read_only_fields = ['id', 'joining_date', 'updated_at']


class UserCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['email', 'full_name', 'password']
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


