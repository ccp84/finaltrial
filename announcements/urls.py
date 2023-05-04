from django.urls import path
from .views import AnnouncementList, MyList, MyDetail, AnnouncementFilter

app_name = 'announcements'

urlpatterns = [
    path('', AnnouncementList.as_view(), name='announcementlist'),
    path('mylist', MyList.as_view(), name='mylist'),
    path('mylist/<int:pk>', MyDetail.as_view(), name='mydetail'),
    path('search', AnnouncementFilter.as_view(), name='announcementsearch')
]
