from django.urls import path
from .views import CustomUserCreate, BlacklistTokenView, CurrentUser

app_name = 'users'

urlpatterns = [
    path('current_user/', CurrentUser.as_view(), name='currentuser'),
    path('register/', CustomUserCreate.as_view(), name='create_user'),
    path('logout/blacklist/', BlacklistTokenView.as_view(), name='blacklist'),
]
