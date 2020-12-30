from django.contrib import admin
from .models import Task, Course

# Registers the Task and Course models to be accessible in the admin page
admin.site.register(Task)
admin.site.register(Course)
