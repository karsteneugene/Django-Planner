from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task


@login_required
def dashboard(request):
    context = {
        'tasks': Task.objects.all()
    }
    return render(request, 'planner/dashboard.html', context)


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'planner/dashboard.html'
    context_object_name = 'tasks'
    ordering = ['date_due']


class TaskDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Task

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = '/'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False


@login_required
def notes(request):
    return render(request, 'planner/notes.html', {'title': 'Notes'})
