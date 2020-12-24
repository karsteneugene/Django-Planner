from django.shortcuts import render
from .models import Task


def dashboard(request):
    context = {
        'tasks': Task.objects.all()
    }
    return render(request, 'planner/dashboard.html', context)


def notes(request):
    return render(request, 'planner/notes.html', {'title': 'Notes'})
