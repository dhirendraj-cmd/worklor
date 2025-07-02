from rest_framework import serializers
from user_profile.profile_models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['bio', 'phone', 'dob']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    
    # serializer = UserProfileSerializer(data=request.data, context={'request': request})



