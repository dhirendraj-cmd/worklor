from django.urls import path
from . import views


app_name = "profile_api_v1"

urlpatterns = [
    path("v1/userprofile/", views.UserProfileView.as_view(), name="userprofile"),
]




