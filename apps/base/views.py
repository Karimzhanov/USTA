from rest_framework import viewsets
from apps.base.models import PageContent, ContentBlock, Partner, Event, EventImage, ProjectParticipation, TeamMember, Ambassador, Education, Сommunities, Membership, Service
from apps.base.serializers import PageContentSerializer, ContentBlockSerializer, PartnerSerializer, EventSerializer, EventImageSerializer, ProjectParticipationSerializer, TeamMemberSerializer, AmbassadorSerializer,EducationSerializer, CommunitiesSerializer, MembershipSerializer, ServiceSerializer

class PageContentViewSet(viewsets.ModelViewSet):
    queryset = PageContent.objects.all()
    serializer_class = PageContentSerializer

    def get_object(self):
        return PageContent.objects.first() or PageContent.objects.create()

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

class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class AmbassadorViewSet(viewsets.ModelViewSet):
    queryset = Ambassador.objects.all()
    serializer_class = AmbassadorSerializer


class AmbassadorViewSet(viewsets.ModelViewSet):
    queryset = Ambassador.objects.all()
    serializer_class = AmbassadorSerializer

class AmbassadorViewSet(viewsets.ModelViewSet):
    queryset = Ambassador.objects.all()
    serializer_class = AmbassadorSerializer

class AmbassadorViewSet(viewsets.ModelViewSet):
    queryset = Ambassador.objects.all()
    serializer_class = AmbassadorSerializer

class AmbassadorViewSet(viewsets.ModelViewSet):
    queryset = Ambassador.objects.all()
    serializer_class = AmbassadorSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class CommunitiesViewSet(viewsets.ModelViewSet):
    queryset = Сommunities.objects.all()
    serializer_class = CommunitiesSerializer

class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer    
