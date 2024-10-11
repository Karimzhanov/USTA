from rest_framework import serializers
from apps.membership.models import Membership, ContentBlock, Category, StepInstruction

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ['id', 'banner', 'title', 'description']

class ContentBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentBlock
        fields = ['id', 'category', 'title', 'image', 'description']
        ref_name = 'MembershipContentBlock'                 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'image']

class StepInstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepInstruction
        fields = ['id', 'step_number', 'title', 'description']
