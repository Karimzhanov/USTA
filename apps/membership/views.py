from rest_framework import viewsets
from apps.membership.models import Membership, ContentBlock, Category, StepInstruction
from apps.membership.serializers import MembershipSerializer, ContentBlockSerializer, CategorySerializer, StepInstructionSerializer

# Create your views here.

class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

class ContentBlockViewSet(viewsets.ModelViewSet):
    queryset = ContentBlock.objects.all()
    serializer_class = ContentBlockSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class StepInstructionViewSet(viewsets.ModelViewSet):
    queryset = StepInstruction.objects.all()
    serializer_class = StepInstructionSerializer
