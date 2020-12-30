from django import forms
from django.forms import ModelForm
from .models import Note


# Uses the Note model so the entered fields can be registered to the Note table
class NoteForm(ModelForm):

    class Meta:
        model = Note
        fields = ['title', 'notes']
