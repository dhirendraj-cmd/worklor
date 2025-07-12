from rest_framework import status
from rest_framework.views import APIView
from .team_serializers import TeamSerializer, TeamCreateSerializer
from rest_framework.response import Response
from team.team_models import Team, Membership
from utils.pagination import CustomPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny


class TeamListCreateView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return Response({
            "message": "Team details will show here"
        })
    
    def post(self, request, format=None, *args, **kwargs):
        serializer = TeamCreateSerializer(data=request.data)
        if serializer.is_valid():
            print("serializer.data>>>>>>>>>>>>> ", serializer.data)
        return Response({
            "message", "team will be saved here"
        })



