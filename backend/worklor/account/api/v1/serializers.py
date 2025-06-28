from rest_framework import serializers
from account.models import User


class UserSerializer(serializers.ModelSerializer):
    joining_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'joining_date', 'updated_at']
        read_only_fields = ['id', 'joining_date', 'updated_at']

