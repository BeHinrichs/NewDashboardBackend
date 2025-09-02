from rest_framework.serializers import ModelSerializer
from .models import Sunset


class SunsetAPISerializer(ModelSerializer):
    class Meta:
        model = Sunset
        fields = [
            "id",
            "date",
            "sunrise",
            "sunset",
            "location",
        ]