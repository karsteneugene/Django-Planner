from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

TYPE_CHOICES = (
    ('Assignment', 'Assignment'),
    ('Project', 'Project'),
)


class Task(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(
        max_length=10, choices=TYPE_CHOICES, default='assignment')
    date_assigned = models.DateField()
    date_due = models.DateField()
    course = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
