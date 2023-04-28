from rest_framework import serializers
from .models import Announcements

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcements
        fields = ['title', 'content', 'author']