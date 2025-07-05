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
    

class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'full_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email).lower()
        instance.full_name = validated_data.get('full_name', instance.full_name)
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        # instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance


