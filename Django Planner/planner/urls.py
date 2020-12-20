from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='planner-dashboard'),
    path('notes/', views.notes, name='planner-notes'),
]
