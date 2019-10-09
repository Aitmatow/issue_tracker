from django.urls import path

from webapp.views import ProjectsList, ProjectsUpdate, ProjectsDetail, ProjectsDelete, ProjectsCreate

urlpatterns = [
    path('', ProjectsList.as_view(), name='projects_list'),
    path('projects/<int:pk>', ProjectsDetail.as_view(), name='projects_view'),
    path('projects/add', ProjectsCreate.as_view(), name='projects_add'),
    path('projects/update/<int:pk>', ProjectsUpdate.as_view(), name='projects_update'),
    path('projects/delete/<int:pk>', ProjectsDelete.as_view(), name='projects_delete'),
]