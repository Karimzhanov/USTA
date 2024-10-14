from rest_framework import serializers
from apps.educert.models import Educert, Contentblock, Videoo

class EducertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educert
        fields = ['id', 'banner', 'title', 'description']

class ContentblockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contentblock
        fields = ['id', 'category', 'title', 'image', 'description']

class VideooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videoo
        fields = ['id', 'title', 'description', 'video_url', 'image']
