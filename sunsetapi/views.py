from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import SunData
from .serializers import SunDataAPISerializer

# Create your views here.
class SunDataAPIView(ListCreateAPIView):
    queryset = SunData.objects.all()
    serializer_class = SunDataAPISerializer