from django.contrib import admin

from tasks.models import Task


class TaskAdmin(admin.ModelAdmin):
    """Регистрация класса Task в
    административной панели Django."""

    list_display = (
        'id',
        'title',
        'description',
        'created_at',
    )
    list_editable = ('description',)
    search_fields = ('title',)
    list_filter = ('created_at',)
    empty_value_display = '-пусто-'


admin.site.register(Task, TaskAdmin)
