# custom imports
from user_profile.profile_models import UserProfile
from .serializers import UserProfileSerializer
from utils.pagination import CustomPagination
from account.models import User

# builtin imports
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated



class UserProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            return self.request.user.profile
        except UserProfile.DoesNotExist:
            raise Http404("User profile does not exist")      
    
    def get(self, request):
        profile = self.get_object()
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)
    
    def put(self, request):
        profile = request.user.profile
        serializer = UserProfileSerializer(profile, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):
        profile = request.user.profile
        serializer = UserProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


