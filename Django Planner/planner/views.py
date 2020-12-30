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
from .forms import TaskForm, CourseForm
from .models import Task, Course


# LoginRequiredMixin -> User needs to be logged in to access the page
# UserPassesTestMixin -> Checks if logged in user is the same with object's user
# SuccessMessageMixin -> returns a success message on a successful action

# Class Based Views for Assignments and Projects

# Dashboard page
class TaskListView(LoginRequiredMixin, ListView):
    model = Task    # Fetch the Task table from the database
    # Renders the dashboard.html template
    template_name = 'planner/dashboard.html'
    context_object_name = 'tasks'   # Assigns a name for all the objects
    ordering = ['date_due']  # Orders tasks by the nearest due date


# Assignments page
class AssignmentListView(LoginRequiredMixin, ListView):
    model = Task    # Fetch the Task table from the database
    # Renders the assignment.html template
    template_name = 'planner/assignment.html'
    context_object_name = 'tasks'   # Assigns a name for all the objects
    ordering = ['date_due']  # Orders tasks by the nearest due date


# Projects page
class ProjectListView(LoginRequiredMixin, ListView):
    model = Task    # Fetch the Task table from the database
    template_name = 'planner/project.html'  # Renders the project.html template
    context_object_name = 'tasks'   # Assigns a name for all the objects
    ordering = ['date_due']  # Orders tasks by the nearest due date


# Expanded task page (More information about each task)
class TaskDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Task    # Fetch the Task table from the database

    # Method to check if the logged in user is the user who made the task, if not, return 403 error
    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False


# Task creation page
class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task    # Fetch the Task table from the database
    form_class = TaskForm   # Fetches the form to create/update notes
    success_url = '/'   # Redirects user to dashboard if creation is successful

    # Displays the specified success message if creation is successful
    success_message = 'Successfully added a task!'

    # Form validation method
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # Method to get dropdown list selections based on the logged in user
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


# Task update page
class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Task    # Fetch the Task table from the database
    form_class = TaskForm   # Fetches the form to create/update notes
    success_url = '/'   # Redirects user to dashboard if update is successful

    # Displays the specified success message if update is successful
    success_message = 'Successfully made changes to a task!'

    # Form validation method
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # Method to get dropdown list selections based on the logged in user
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    # Method to check if the logged in user is the user who made the task, if not, return 403 error
    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False


# Task deletion page
class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task    # Fetch the Task table from the database
    success_url = '/'   # Redirects user to dashboard if deletion is successful

    # Method to check if the logged in user is the user who made the task, if not, return 403 error
    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False


# Class Based Views for Courses

# Main Courses page
class CourseListView(LoginRequiredMixin, ListView):
    model = Course  # Fetch the Course table from the database
    template_name = 'planner/course.html'   # Renders the course.html template
    context_object_name = 'courses'  # Assigns a name for all the objects


# Tasks page that only contains the Course you clicked in the Main Courses page
class CourseDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Course  # Fetch the Course table from the database

    # Method to fetch the Task table into the page
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context

    # Method to check if the logged in user is the user who made the course, if not, return 403 error
    def test_func(self):
        course = self.get_object()
        if self.request.user == course.user:
            return True
        return False


# Course creation page
class CourseCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Course  # Fetch the Course table from the database
    form_class = CourseForm  # Fetches the form to create courses

    # Redirects user to main courses page if creation is successful
    success_url = '/courses/'

    # Displays the specified success message if creation is successful
    success_message = 'Successfully added a course!'

    # Form validation method
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Course delete
class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Course  # Fetch the Course table from the database

    # Redirects user to main courses page if deletion is successful
    success_url = '/courses/'

    # Method to check if the logged in user is the user who made the course, if not, return 403 error
    def test_func(self):
        course = self.get_object()
        if self.request.user == course.user:
            return True
        return False
