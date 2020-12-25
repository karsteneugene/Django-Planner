from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task


@login_required
def dashboard(request):
    context = {
        'tasks': Task.objects.all()
    }
    return render(request, 'planner/dashboard.html', context)


@login_required
def notes(request):
    return render(request, 'planner/notes.html', {'title': 'Notes'})
