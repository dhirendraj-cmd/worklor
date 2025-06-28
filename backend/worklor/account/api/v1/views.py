from account.models import User
from .serializers import UserSerializer
from rest_framework import viewsets
# from rest_framework.pagination import PageNumberPagination


class UserApiView(viewsets.ReadOnlyModelViewSet):
    """
        Provide list of all users
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    # pagination_class = Pa

    

