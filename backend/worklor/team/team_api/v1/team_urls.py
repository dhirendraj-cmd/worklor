from django.urls import path
from . import team_views

app_name = 'team_api_v1'

urlpatterns = [
    path("v1/teams/", team_views.TeamListCreateView.as_view(), name="teams"),
]


