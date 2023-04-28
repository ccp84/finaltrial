from django.urls import path
from django.views.generic import TemplateView
from .views import AnnouncementList, AnnouncementDetail

urlpatterns = [
    path('', TemplateView.as_view(template_name="announcements/index.html")),
    path('api', AnnouncementList.as_view(), name='announcementlist'),
    path('api/<int:pk>', AnnouncementDetail.as_view(), name='announcementdetail'),
]