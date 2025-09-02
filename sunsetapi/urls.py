from django.urls import path
from .views import SunsetAPIView

urlpatterns = [
    path('api/', SunsetAPIView.as_view())
]