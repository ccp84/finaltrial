from rest_framework import generics
from .models import Announcements
from .serializers import AnnouncementSerializer


class AnnouncementList(generics.ListCreateAPIView):
    queryset = Announcements.objects.all()
    serializer_class = AnnouncementSerializer


class AnnouncementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcements.objects.all()
    serializer_class = AnnouncementSerializer
