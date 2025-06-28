from django.urls import path, include
from rest_framework import routers, urlpatterns
from . import views


app_name = "account_api_v1"

router = routers.DefaultRouter()
router.register("userlist", views.UserApiView, basename="userlist")



urlpatterns = [
    path('v1/', include(router.urls)),
]


