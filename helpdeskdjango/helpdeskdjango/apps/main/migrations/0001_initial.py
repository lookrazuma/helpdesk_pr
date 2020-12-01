# Generated by Django 3.1.3 on 2020-11-30 11:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=50, verbose_name='Название статуса')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('host_name', models.CharField(default='B10-001-001', max_length=50, verbose_name='Хост компьютера')),
                ('dept', models.CharField(default='Бухгалтерия', max_length=50, verbose_name='Отдел работы')),
                ('task', models.TextField(verbose_name='Описание')),
                ('author', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('status_task', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='main.status')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'permissions': (('can_mark_returned', 'Set book as returned'),),
            },
        ),
    ]
