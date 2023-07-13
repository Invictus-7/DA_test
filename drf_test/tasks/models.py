from django.db import models


class Task(models.Model):
    """Модель для создания заданий."""

    title = models.CharField('Название задания', max_length=255)
    description = models.TextField('Текст задания')
    created_at = models.DateTimeField('Время создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
