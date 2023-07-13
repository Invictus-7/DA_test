from rest_framework import generics

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    """View-класс для создания заданий и получения
    их полного списка."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """View-класс для редактирования, удаления
    и просмотра отдельных заданий."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
