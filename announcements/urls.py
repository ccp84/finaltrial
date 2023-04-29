from django.urls import path
from .views import AnnouncementList, AnnouncementDetail

urlpatterns = [
    path('', AnnouncementList.as_view(), name='announcementlist'),
    path('<int:pk>', AnnouncementDetail.as_view(), name='announcementdetail'),
]
