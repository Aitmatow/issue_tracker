from django.urls import path, include
from rest_framework import routers

from api.views import ProjectsViewSet, IssueViewSet

router = routers.DefaultRouter()
router.register(r'issues', IssueViewSet)
router.register(r'projects', ProjectsViewSet)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls' , namespace = 'rest_framework'))
]