from rest_framework.serializers import ModelSerializer
from .models import SunData


class SunDataAPISerializer(ModelSerializer):
    class Meta:
        model = SunData
        fields = [
            "date",
            "sunrise",
            "sunset",
        ]