from rest_framework import serializers
from apps.ambassadorship.models import Ambassadorship, AmbassadorshipImage

class AmbassadorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambassadorship
        fields = ['id', 'banner', 'title', 'description']

class AmbassadorshipImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmbassadorshipImage
        fields = ['id', 'image', 'description']
