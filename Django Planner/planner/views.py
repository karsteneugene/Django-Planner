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
from .forms import TaskForm, CourseForm
from .models import Task, Course


# Views for Assignments and Projects
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'planner/dashboard.html'
    context_object_name = 'tasks'
    ordering = ['date_due']


class AssignmentListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'planner/assignment.html'
    context_object_name = 'tasks'
    ordering = ['date_due']


class ProjectListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'planner/project.html'
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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


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


# Views for Courses
class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'planner/course.html'
    context_object_name = 'courses'


class CourseDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context

    def test_func(self):
        course = self.get_object()
        if self.request.user == course.user:
            return True
        return False


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    success_url = '/courses/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Course
    success_url = '/courses/'

    def test_func(self):
        course = self.get_object()
        if self.request.user == course.user:
            return True
        return False


@login_required
def notes(request):
    return render(request, 'planner/notes.html', {'title': 'Notes'})
