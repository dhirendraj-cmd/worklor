from django.urls import path, include

urlpatterns = [
    path("v1/", include("worklor_api.api.v1.urls", namespace="v1")),
]


