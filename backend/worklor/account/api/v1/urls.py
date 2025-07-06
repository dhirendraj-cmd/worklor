from django.urls import path, include
# from rest_framework import routers, urlpatterns
from . import views


app_name = "account_api_v1"

# router = routers.DefaultRouter()
# router.register("userlist", views.UserApiView, basename="userlist")



urlpatterns = [
    # path('v1/', include(router.urls)),
    path("v1/userslist/", views.UserListCreateView.as_view(), name="userslist"),
    path("v1/userdetail/<str:pk>/", views.UserDetailUpdateView.as_view(), name="userdetail"),
]


