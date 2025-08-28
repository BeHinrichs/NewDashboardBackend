from rest_framework.serializers import ModelSerializer
from .models import Task


class TaskAPISerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "name",
            "create_by",
            "title",
            "status",
            "checked",
        ]