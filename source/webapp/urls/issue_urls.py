from django.urls import path

from webapp.views import IssueDetail, IssueUpdate, IssueDelete, IssueCreate, IssueList

urlpatterns = [
    path('', IssueList.as_view(), name='issue_list'),
    path('issue/<int:pk>', IssueDetail.as_view(), name='issue_view'),
    path('issue/add', IssueCreate.as_view(), name='add_issue'),
    path('issue/update/<int:pk>', IssueUpdate.as_view(), name='issue_update'),
    path('issue/delete/<int:pk>', IssueDelete.as_view(), name='issue_delete'),
]