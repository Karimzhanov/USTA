from rest_framework import serializers
from apps.about_the_community.models import About, CommunityImage

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'banner', 'title', 'description']

class CommunityImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityImage
        fields = ['id', 'image', 'description']
