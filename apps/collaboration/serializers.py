from rest_framework import serializers
from apps.collaboration.models import Сollaboration, Project, ProjectsPage, Award, MentoringPrograms

class СollaborationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Сollaboration
        fields = ['id', 'banner', 'title', 'description']  

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'image', 'title', 'description']  

class ProjectsPageSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True)  

    class Meta:
        model = ProjectsPage
        fields = ['id', 'title', 'projects']  
class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ['id', 'image', 'title', 'description']  

class MentoringProgramsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentoringPrograms
        fields = ['id', 'title', 'image', 'description', 'additional_text']  
