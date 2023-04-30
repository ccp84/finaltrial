from django.urls import path
from .views import AnnouncementList, AnnouncementDetail

app_name = 'announcements'

urlpatterns = [
    path('', AnnouncementList.as_view(), name='announcementlist'),
    path('<int:pk>', AnnouncementDetail.as_view(), name='announcementdetail'),
]
