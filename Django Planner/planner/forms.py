from django import forms
from django.forms import ModelForm
from .models import Task, Course


# Creates a widget to be used for inputting dates
class DateInput(forms.DateInput):
    input_type = 'date'


# Uses the Course model so the entered fields can be registered to the Course table
class CourseForm(ModelForm):

    class Meta:
        model = Course
        fields = ['course_name']


# Uses the Task model so the entered fields can be registered to the Task table
class TaskForm(ModelForm):

    # Displays only the courses registered by the logged in user
    def __init__(self, user, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.filter(user=user)

    class Meta:
        model = Task
        fields = ['title', 'type', 'date_assigned',
                  'date_due', 'course', 'description']
        # Date input widgets used for 'date assigned' and 'date due'
        widgets = {
            'date_assigned': DateInput(),
            'date_due': DateInput(),
        }
