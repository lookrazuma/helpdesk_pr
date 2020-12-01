from django.contrib import admin

from .models import Task, status

admin.site.register(Task)
admin.site.register(status)

