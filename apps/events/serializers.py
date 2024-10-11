from rest_framework import serializers
from .models import Events, Eventss, Announcement, AnnualEvent, VideoContent, VideoContents

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id', 'banner', 'title', 'description']  


class EventssSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventss
        fields = ['id', 'title', 'image', 'date']  

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'title', 'description']


class AnnualEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnualEvent
        fields = ['id', 'image', 'title'] 


class VideoContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoContent
        fields = ['id', 'thumbnail', 'title', 'description', 'video_url']  


class VideoContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoContents
        fields = ['id', 'thumbnail', 'title', 'description', 'video_url']  