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


class NotesListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/notes.html'
    context_object_name = 'notes'
    ordering = ['-date_updated']


class NotesDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Note

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False


class NotesCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Note
    form_class = NoteForm
    success_url = '/notes/'
    success_message = 'Note created!'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NotesUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Note
    form_class = NoteForm
    success_url = '/notes/'
    success_message = 'Note updated!'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.user:
            return True
        return False


class NotesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    success_url = '/notes/'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False
