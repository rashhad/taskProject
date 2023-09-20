from typing import Any
from django.forms import ModelForm
from . import models


class AddTaskForm(ModelForm):
    class Meta:
        model=models.TaskModel
        fields=['taskTitle','taskDescription']

