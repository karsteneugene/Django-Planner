from django.shortcuts import render


tasks = [
    {
        'title': 'Python Programming Exercise 12',
        'type': 'Assignment',
        'date_assigned': '1 December',
        'date_due': '8 December',
        'course': 'Program Design Methods',
        'description': '<Objective for this task>'
    },
    {
        'title': 'Regular Expressions',
        'type': 'Assignment',
        'date_assigned': '5 December',
        'date_due': '12 December',
        'course': 'Discrete Structures',
        'description': '<Objective for this task>'
    },
    {
        'title': 'Alien Invasion',
        'type': 'Project',
        'date_assigned': '1 December',
        'date_due': '1 January',
        'course': 'Program Design Methods',
        'description': '<Objective for this task>'
    }
]


def dashboard(request):
    context = {
        'tasks': tasks
    }
    return render(request, 'planner/dashboard.html', context)


def notes(request):
    return render(request, 'planner/notes.html', {'title': 'Notes'})
