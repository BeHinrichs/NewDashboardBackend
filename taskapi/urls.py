from django.urls import path
from .views import TaskAPIView, updateTaskAPIView

urlpatterns = [
    path('tasks/', TaskAPIView.as_view()),
    path('tasks/<int:pk>/', updateTaskAPIView.as_view())
]