from django.db import models
from django.contrib.auth.models import User


TYPE_CHOICES = (
    ('Assignment', 'Assignment'),
    ('Project', 'Project'),
)


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name


class Task(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(
        max_length=10, choices=TYPE_CHOICES, default='assignment')
    date_assigned = models.DateField()
    date_due = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
