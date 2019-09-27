from django.urls import path

from webapp import views
from webapp.views import TipsList, TipsDetail, \
    TipsCreate, TipsUpdate, TipsDelete

urlpatterns = [
    path('', TipsList.as_view(), name='tips_list'),
    path('tips/<int:pk>', TipsDetail.as_view(), name='tips_view'),
    path('tips/add', TipsCreate.as_view(), name='tips_new'),
    path('tips/update/<int:pk>', TipsUpdate.as_view(), name='tips_edit'),
    path('tips/delete/<int:pk>', TipsDelete.as_view(), name='tips_delete')
    ]