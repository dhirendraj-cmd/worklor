from django.urls import path
from . import views

app_name = "worklor_api_v1"

urlpatterns = [
    path("index/", views.index, name="index"),
]


