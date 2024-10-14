from rest_framework import viewsets
from apps.collaboration.models import Сollaboration, Project, ProjectsPage, Award, MentoringPrograms
from apps.collaboration.serializers import СollaborationSerializer, ProjectSerializer, ProjectsPageSerializer, AwardSerializer,MentoringProgramsSerializer

# Create your views here.

class СollaborationViewSet(viewsets.ModelViewSet):
    queryset = Сollaboration.objects.all()
    serializer_class = СollaborationSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectsPageViewSet(viewsets.ModelViewSet):
    queryset = ProjectsPage.objects.all()
    serializer_class = ProjectsPageSerializer

class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

class MentoringProgramsViewSet(viewsets.ModelViewSet):
    queryset = MentoringPrograms.objects.all()
    serializer_class = MentoringProgramsSerializer
