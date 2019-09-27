from django.urls import path

from webapp import views
from webapp.views import StatusList, StatusDetail, \
    StatusCreate, StatusUpdate, StatusDelete

urlpatterns = [
    path('', StatusList.as_view(), name='status_list'),
    path('status/<int:pk>', StatusDetail.as_view(), name='status_view'),
    path('status/add', StatusCreate.as_view(), name='status_new'),
    path('status/update/<int:pk>', StatusUpdate.as_view(), name='statuses_edit'),
    path('status/delete/<int:pk>', StatusDelete.as_view(), name='status_delete')
    ]