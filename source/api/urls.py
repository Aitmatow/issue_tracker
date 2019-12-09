from django.urls import path, include
from rest_framework import routers

from api.views import ProjectsViewSet, IssueViewSet, LogoutView
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'issues', IssueViewSet)
router.register(r'projects', ProjectsViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name='delete_auth_token')
]