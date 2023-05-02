from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/', BlacklistTokenUpdateView.as_view(),
         name='logout')
]
