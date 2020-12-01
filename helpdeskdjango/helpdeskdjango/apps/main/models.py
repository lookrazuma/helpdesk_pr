from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse 

class status(models.Model):
    status_name = models.CharField('Название статуса', max_length = 50,)

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'



class Task(models.Model):
    title = models.CharField('Название', max_length = 50)
    author = models.ForeignKey(User,on_delete=models.CASCADE, default=None, blank=True)
    host_name = models.CharField('Хост компьютера', max_length = 50, default='B10-001-001')
    dept = models.CharField('Отдел работы', max_length = 50, default='Бухгалтерия')
    task = models.TextField('Описание')
    status_task = models.ForeignKey(status, on_delete = models.CASCADE, default='1')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        permissions = (("can_mark_returned", "Set book as returned"),)


    def get_absolute_url(self):
        return reverse("manage_details_url", kwargs={"task_id": self.pk})

    def get_update_url(self):
        return reverse("manage_update_url", kwargs={"task_id": self.pk})
