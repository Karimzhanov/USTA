from django.shortcuts import render
from rest_framework import viewsets
from apps.educert.models import Educert, Contentblock, Videoo
from apps.educert.serializers import EducertSerializer, ContentblockSerializer, VideooSerializer

# Create your views here.

class EducertViewSet(viewsets.ModelViewSet):
    queryset = Educert.objects.all()
    serializer_class = EducertSerializer

class ContentblockViewSet(viewsets.ModelViewSet):
    queryset = Contentblock.objects.all()
    serializer_class = ContentblockSerializer

class VideooViewSet(viewsets.ModelViewSet):
    queryset = Videoo.objects.all()  
    serializer_class = VideooSerializer  
