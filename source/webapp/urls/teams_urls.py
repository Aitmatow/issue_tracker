from django.urls import path

from webapp import views
from webapp.views import  \
    TeamsCreate, TeamsDelete

urlpatterns = [
    path('teams/add/<int:pk>', TeamsCreate.as_view(), name='teams_new'),
    path('teams/delete/<int:pk>', TeamsDelete.as_view(), name='teams_delete')
    ]