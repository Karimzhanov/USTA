from rest_framework import viewsets
from apps.base.models import PageContent, ContentBlock, Partner, Event, EventImage, ProjectParticipation, ProjectImage, TeamMember, ContentBlocks
from apps.base.serializers import PageContentSerializer, ContentBlockSerializer, PartnerSerializer, EventSerializer, EventImageSerializer, ProjectParticipationSerializer, ProjectImageSerializer, TeamMemberSerializer, ContentBlocksSerializer

class PageContentViewSet(viewsets.ModelViewSet):
    queryset = PageContent.objects.all()
    serializer_class = PageContentSerializer

class ContentBlockViewSet(viewsets.ModelViewSet):
    queryset = ContentBlock.objects.all()
    serializer_class = ContentBlockSerializer

class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventImageViewSet(viewsets.ModelViewSet):
    queryset = EventImage.objects.all()
    serializer_class = EventImageSerializer

class ProjectParticipationViewSet(viewsets.ModelViewSet):
    queryset = ProjectParticipation.objects.all()
    serializer_class = ProjectParticipationSerializer

class ProjectImageViewSet(viewsets.ModelViewSet):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer

class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class ContentBlocksViewSet(viewsets.ModelViewSet):
    queryset = ContentBlocks.objects.all()
    serializer_class = ContentBlocksSerializer
