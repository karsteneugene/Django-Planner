from django.db import models
from django.contrib.auth.models import User


# Creates a database table for notes with the fields below
class Note(models.Model):
    title = models.CharField(max_length=200)
    notes = models.TextField()

    # Automatically adds a date of when the note is first created
    date_created = models.DateTimeField(auto_now_add=True)

    # Automatically updates the date when the content of the notes is updated
    date_updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
