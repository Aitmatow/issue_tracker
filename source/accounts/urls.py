from django.urls import path
from accounts.views import login_view, logout_view, register_view, user_activation_view, UserDetailView, \
    UserPersonalInfoChangeView, UserPasswordChangeView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('activate/<token>/', user_activation_view, name='user_activate'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('<int:pk>/update', UserPersonalInfoChangeView.as_view(), name='update'),
    path('<int:pk>/password_change', UserPasswordChangeView.as_view(), name='password_change')
]

app_name = 'accounts'