from django.urls import path

from webapp import views
from webapp.views import TeamsList, TeamsDetail, \
    TeamsCreate, TeamsUpdate, TeamsDelete

urlpatterns = [
    path('', TeamsList.as_view(), name='teams_list'),
    path('teams/<int:pk>', TeamsDetail.as_view(), name='teams_view'),
    path('teams/add/<int:pk>', TeamsCreate.as_view(), name='teams_new'),
    path('teams/update/<int:pk>', TeamsUpdate.as_view(), name='teams_edit'),
    path('teams/delete/<int:pk>', TeamsDelete.as_view(), name='teams_delete')
    ]