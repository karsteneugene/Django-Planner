from django.urls import path
from .views import (
    TaskListView,
    AssignmentListView,
    ProjectListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    CourseListView,
    CourseDetailView,
    CourseCreateView,
    CourseDeleteView
)
from . import views


urlpatterns = [
    path('', TaskListView.as_view(), name='planner-dashboard'),
    path('assignments/', AssignmentListView.as_view(), name='planner-assignments'),
    path('projects/', ProjectListView.as_view(), name='planner-projects'),
    path('projects/', TaskListView.as_view(), name='planner-projects'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('courses/', CourseListView.as_view(), name='planner-courses'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/new/', CourseCreateView.as_view(), name='course-add'),
    path('courses/<int:pk>/delete/',
         CourseDeleteView.as_view(), name='course-delete'),
]
