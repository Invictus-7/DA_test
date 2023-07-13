from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from tasks.models import Task


class TaskTests(APITestCase):
    """Класс для тестирования приложения Task."""

    def setUp(self):
        """Создаем фикстуры - пробный объект Task и URL
        для избегания дублирования кода в трёх последних тестах."""
        self.task = Task.objects.create(title='Task 1',
                                        description='Test task')
        self.url = reverse('task-retrieve-update-delete',
                           kwargs={'pk': self.task.pk})

    def test_create_task(self):
        """Тест для проверки работы метода,
        создающего объект."""
        # Для этого теста удаляем созданный в фикстурах объект,
        # иначе метод get будет возвращать ошибку.
        if self.task:
            self.task.delete()
        url = reverse('task-list-create')
        data = {
            'title': 'Task 1',
            'description': 'Test description for Task 1',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Task 1')
        self.assertEqual(Task.objects.get().description,
                         'Test description for Task 1')

    def test_get_task_list(self):
        """Тест для проверки работы метода,
        возвращающего список объектов."""
        url = reverse('task-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_task_detail(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        data = {
            'title': 'Updated Task 1',
            'description': 'Updated Task 1',
        }
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get().title, 'Updated Task 1')
        self.assertEqual(Task.objects.get().description, 'Updated Task 1')

    def test_delete_task(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
