from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Note
from .forms import NoteForm


# LoginRequiredMixin -> User needs to be logged in to access the page
# UserPassesTestMixin -> Checks if logged in user is the same with object's user
# SuccessMessageMixin -> returns a success message on a successful action


# Main Notes page
class NotesListView(LoginRequiredMixin, ListView):
    model = Note    # Fetch the Note table from the database
    template_name = 'notes/notes.html'  # Renders the notes.html template
    context_object_name = 'notes'   # Assigns a name for all the objects
    ordering = ['-date_updated']    # Orders notes by recently updated first


# Expanded note page
class NotesDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Note    # Fetch the Note table from the database

    # Automatically renders note_detail.html template

    # Method to check if the logged in user is the user who made the note, if not, return 403 error
    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False


# Note creation page
class NotesCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Note    # Fetch the Note table from the database
    form_class = NoteForm   # Fetches the form to create/update notes
    success_url = '/notes/'  # Redirects user to main notes page if creation is successful

    # Displays the specified success message if creation is successful
    success_message = 'Note created!'

    # Form validation method
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Note update page
class NotesUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Note    # Fetch the Note table from the database
    form_class = NoteForm   # Fetches the form to create/update notes
    success_url = '/notes/'  # Redirects user to main notes page if update is successful

    # Displays the specified success message if update is successful
    success_message = 'Note updated!'

    # Form validation method
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # Method to check if the logged in user is the user who made the note, if not, return 403 error
    def test_func(self):
        note = self.get_object()
        if self.request.user == note.user:
            return True
        return False


# Note deletion page
class NotesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note    # Fetch the Note table from the database
    success_url = '/notes/'  # Redirects user to main notes page if deletion is successful

    # Method to check if the logged in user is the user who made the note, if not, return 403 error
    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False
