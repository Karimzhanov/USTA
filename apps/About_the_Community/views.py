from rest_framework import viewsets
from apps.about_the_community.models import About, CommunityImage
from apps.about_the_community.serializers import AboutSerializer, CommunityImageSerializer

# Create your views here.

class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class CommunityImageViewSet(viewsets.ModelViewSet):
    queryset = CommunityImage.objects.all()
    serializer_class = CommunityImageSerializer
