from django import forms
from .models import TaskModels

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = TaskModels
        fields = ['task_name', 'task_descp', 'task_status']


    