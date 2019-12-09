from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
import django_filters.rest_framework
from api.serializers import IssueSerializer, ProjectsSerializer
from webapp.models import Issue, Projects
from rest_framework.permissions import IsAuthenticated, AllowAny, SAFE_METHODS, DjangoModelPermissions

# Create your views here.
# Проекты, задачи

'''$.ajax({ 
data : JSON.stringify({username: 'admin', password : 'admin'}),
method: 'post',
url : 'http://localhost:8000/api/v1/login/',
contentType:'application/json',
dataType : 'json',
success:function(response, status) {console.log(response);},
error: function(response, status) {console.log(response);}
});'''

'''$.ajax({ 
data : JSON.stringify({username: 'admin', password : 'admin'}),
method: 'post',
url : 'http://localhost:8000/api/v1/login/',
contentType:'application/json',
dataType : 'json',
success:function(response, status) {console.log(response); localStorage.setItem('api_token', response.token);},
error: function(response, status) {console.log(response);}
});'''

'''$.ajax({ 
method: 'get',
url : 'http://localhost:8000/api/v1/issues/',
headers : {'Authorization' : 'Token a4082ec63855a33e525bff59728218f76ebcf736' },
dataType : 'json',
success:function(response, status) {console.log(response);},
error: function(response, status) {console.log(response);}
});'''

'''$.ajax({ 
method: 'post',
url : 'http://localhost:8000/api/v1/logout/',
dataType : 'json',
success:function(response, status) {console.log(response);},
error: function(response, status) {console.log(response);}
});'''

class CustomDjangoModelPermission(DjangoModelPermissions):
    def __init__(self):
        self.perms_map['POST'] = ['%(app_label)s.view_%(model_name)s']
        self.perms_map['DELETE'] = ['%(app_label)s.view_%(model_name)s']

class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})


class IssueViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomDjangoModelPermission]
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['project']
    # def get_permissions(self):
    #     if self.request.method in SAFE_METHODS:
    #         return [AllowAny()]
    #     else:
    #         return super().get_permissions()



class ProjectsViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectsSerializer
    queryset = Projects.objects.all()

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        else:
            return super().get_permissions()
