from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с моделью Task."""

    class Meta:
        model = Task
        # явно указываем всем поля модели
        fields = (
            'id',
            'title',
            'created_at',
            'description',
        )
