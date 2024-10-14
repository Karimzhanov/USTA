from rest_framework import viewsets
from apps.ambassadorship.models import Ambassadorship, AmbassadorshipImage
from apps.ambassadorship.serializers import AmbassadorshipSerializer, AmbassadorshipImageSerializer

# Create your views here.

class AmbassadorshipViewSet(viewsets.ModelViewSet):
    queryset = Ambassadorship.objects.all()
    serializer_class = AmbassadorshipSerializer

class AmbassadorshipImageViewSet(viewsets.ModelViewSet):
    queryset = AmbassadorshipImage.objects.all()
    serializer_class = AmbassadorshipImageSerializer
