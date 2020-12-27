from django import forms
from django.forms import ModelForm
from .models import Task, Course


class DateInput(forms.DateInput):
    input_type = 'date'


class CourseForm(ModelForm):

    class Meta:
        model = Course
        fields = ['course_name']


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'type', 'date_assigned',
                  'date_due', 'course', 'description']
        widgets = {
            'date_assigned': DateInput(),
            'date_due': DateInput(),
        }
