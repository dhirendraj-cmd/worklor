from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # worklor_api versioned endpoint
    path('api/v1/', include('worklor_api.api.v1.urls', namespace="worklor_api_v1")),

    # account app versioned endpoint
    path('account/', include('account.api.v1.urls', namespace="account_api_v1")),
    # profile app versioned endpoint
    path('profile/', include('user_profile.api.v1.urls', namespace="profile_api_v1")),
    # team app versioned endpoint
    path('team/', include('team.team_api.v1.team_urls', namespace="team_api_v1")),
    # task app versioned endpoint
    # path('task/', include('task.task_api.v1.task_urls', namespace="task_api_v1")),
]

if settings.DEBUG:
    urlpatterns += [
        path('api-auth/', include('rest_framework.urls')),
    ]


