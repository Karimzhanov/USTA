from rest_framework import serializers
from apps.base.models import PageContent, ContentBlock, Partner, Event, EventImage, ProjectParticipation, ProjectImage,TeamMember, Ambassador, Education, Сommunities, Membership, Service

class PageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContent
        fields = ['logo', 'banner', 'title', 'description']


class ContentBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentBlock
        fields = ['id', 'title', 'description', 'date', 'image']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'name', 'logo']

class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ['id', 'image', 'event']

class EventSerializer(serializers.ModelSerializer):
    images = EventImageSerializer(many=True, read_only=True) 

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'images']

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['id', 'image']

class ProjectParticipationSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = ProjectParticipation
        fields = ['id', 'title', 'description', 'additional_text', 'images']


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['id', 'full_name', 'position', 'photo']   


class AmbassadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambassador
        fields = ['id', 'title', 'description', 'additional_text', 'image']

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'title', 'description', 'additional_text', 'image']

class CommunitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Сommunities
        fields = ['id', 'title', 'description', 'additional_text', 'image']

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ['id', 'title', 'description', 'additional_text', 'image']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'additional_text', 'image']

