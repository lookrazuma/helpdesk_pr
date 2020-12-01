from .models import Task
from django import forms
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = {'title','host_name','dept','task', 'author'}
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "host_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "dept": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            })
        }

    