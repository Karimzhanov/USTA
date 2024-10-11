from rest_framework import serializers
from .models import PageContent, ContentBlock, Partner, Event, EventImage, ProjectParticipation, ProjectImage, TeamMember, ContentBlocks

class PageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContent
        fields = ['id', 'logo', 'banner', 'title', 'description']

class ContentBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentBlock
        fields = ['id', 'title', 'description', 'date', 'image']
        ref_name = 'BaseContentBlock'  

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'logo', 'name']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'additional_text']

class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ['id', 'image', 'event']

class ProjectParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectParticipation
        fields = ['id', 'title', 'description', 'additional_text']

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['id', 'image', 'project']

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['id', 'full_name', 'position', 'photo']

class ContentBlocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentBlocks
        fields = ['id', 'category', 'title', 'image', 'description', 'additional_text']
