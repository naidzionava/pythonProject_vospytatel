from . models import Task
from django.forms import ModelForm, TextInput, Textarea


class Taskform(ModelForm):
    class Meta:
        model = Task
        fields = ["title","task"]
        widgets = {
            "title": TextInput(attrs={
            'class': 'from-control',
            "placeholder": "Введите название"
        }),
            "task": Textarea(attrs={
            'class': 'from-control',
            "placeholder": "Введите описание"
        }),

        }