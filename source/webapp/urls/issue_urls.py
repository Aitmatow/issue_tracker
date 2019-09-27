from django.urls import path

from webapp.views import IndexView, IssueView, IssueCreate, IssueUpdate, IssueDelete, StatusList, StatusDetail, \
    StatusCreate, StatusUpdate, StatusDelete

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('issue/<int:pk>', IssueView.as_view(), name='issue_view'),
    path('issue/add', IssueCreate.as_view(), name='add_issue'),
    path('issue/update/<int:pk>', IssueUpdate.as_view(), name='issue_update'),
    path('issue/delete/<int:pk>', IssueDelete.as_view(), name='issue_delete'),
]