from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Sunset
from .serializers import SunsetAPISerializer

# Create your views here.
class SunsetAPIView(ListCreateAPIView):
    queryset = Sunset.objects.all()
    serializer_class = SunsetAPISerializer