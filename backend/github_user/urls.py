from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .rest import *

app_name='github_user'

urlpatterns=[
    path('', GithubUserList.as_view()),
    path('<int:pk>/', api_githubUser_detail),
    path('projects/', api_githubUser_projects ),
    path('teams/', api_githubUser_teams ),
    path('loggedIn/',api_githubUser_loggedIn)
]