from account.models import User
from .serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from utils.pagination import CustomPagination



class UserListCreateView(APIView):
    """
        Provide list of all users and create new one
    """
    # permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        elif self.request.method == 'POST':
            return [AllowAny()]
        return super().get_permissions()

    def get(self, request, format=None):
        users = User.objects.all().order_by('-updated_at')
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(users, request)
        serializer = UserSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Use nested UserSerializer to return full detail with profile
            response_serializer = UserSerializer(user)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class UserDetailUpdateView(APIView):

    """
        Retrieving, updating and deleting user
    """

    def get_permissions(self):
        if self.request.method in ["DELETE", "PUT", "GET"]:
            return [IsAuthenticated()]
        return super().get_permissions()
    
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404("User not found.")
        
    def get(self, request, pk, format=None):
        user = self.get_object(pk=pk)
        serializer  = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk=pk)

        # checking if same user doing updates
        if request.user != user and not request.user.is_staff:
            return Response(
                {'detail': 'Not authorized.'},
                status=status.HTTP_403_FORBIDDEN
                )
        
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            updated_user = serializer.save()
            response_serializer = UserSerializer(updated_user)
            return Response(response_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        user = self.get_object(pk=pk)

        # checking if same user doing delete
        if request.user != user and not request.user.is_staff:
            return Response(
                {'detail': 'Not authorized.'},
                status=status.HTTP_403_FORBIDDEN
                )
        
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

