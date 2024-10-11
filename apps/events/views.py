from rest_framework import viewsets
from apps.events.models import Events, Eventss, Announcement, AnnualEvent, VideoContent, VideoContents
from apps.events.serializers import EventsSerializer, EventssSerializer,AnnouncementSerializer,AnnualEventSerializer, VideoContentSerializer,VideoContentsSerializer
# Create your views here.

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


class EventssViewSet(viewsets.ModelViewSet):
    queryset = Eventss.objects.all()
    serializer_class = EventssSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class AnnualEventViewSet(viewsets.ModelViewSet):
    queryset = AnnualEvent.objects.all()
    serializer_class = AnnualEventSerializer


class VideoContentViewSet(viewsets.ModelViewSet):
    queryset = VideoContent.objects.all()
    serializer_class = VideoContentSerializer


class VideoContentsViewSet(viewsets.ModelViewSet):
    queryset = VideoContents.objects.all()
    serializer_class = VideoContentsSerializer
