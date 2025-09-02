from django.urls import path
from .views import TaskAPIView, updateTaskAPIView

urlpatterns = [
    path('api/', TaskAPIView.as_view()),
    path('api/<int:pk>/', updateTaskAPIView.as_view())
]