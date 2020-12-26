from django import forms
from django.forms import ModelForm
from .models import Task


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'type', 'date_assigned',
                  'date_due', 'course', 'description']
        widgets = {
            'date_assigned': DateInput(),
            'date_due': DateInput(),
        }
