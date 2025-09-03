from django.urls import path
from .views import SunDataAPIView

urlpatterns = [
    path('api/', SunDataAPIView.as_view())
]