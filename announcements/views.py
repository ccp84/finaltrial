from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework import permissions, filters
from .models import Announcements
from .serializers import AnnouncementSerializer


class OwnerWritePermission(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    message = "Editing posts is restricted to author only"

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.author == request.user


class AnnouncementList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AnnouncementSerializer
    queryset = Announcements.objects.all()


class MyList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AnnouncementSerializer

    def get_queryset(self):
        """
            Override the standard query set and filter
            """
        user = self.request.user
        return Announcements.objects.filter(author=user)


class MyDetail(generics.RetrieveUpdateDestroyAPIView, OwnerWritePermission):
    permission_classes = [OwnerWritePermission]
    serializer_class = AnnouncementSerializer

    def get_queryset(self):
        """
            Override the standard query set and filter
            """
        user = self.request.user
        return Announcements.objects.filter(author=user)


class AnnouncementFilter(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AnnouncementSerializer
    queryset = Announcements.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['content']
