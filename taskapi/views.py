from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Task
from .serializers import TaskAPISerializer

# Create your views here.
class TaskAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskAPISerializer

class updateTaskAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskAPISerializer

