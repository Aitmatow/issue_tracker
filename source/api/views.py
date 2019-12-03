from django.shortcuts import render
from rest_framework import viewsets

from api.serializers import IssueSerializer, ProjectsSerializer
from webapp.models import Issue, Projects

# Create your views here.
# Проекты, задачи
class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()


class ProjectsViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectsSerializer
    queryset = Projects.objects.all()