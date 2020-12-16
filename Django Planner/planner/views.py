from django.shortcuts import render


to_do_list = [
    {
        'day': '25 December',
        'to_do_1': 'Grab breakfast',
        'to_do_2': 'Meet up friends',
        'to_do_3': 'Work out',
        'notes': 'Remember, you are on a diet!'
    },
    {
        'day': '26 December',
        'to_do_1': 'Grab breakfast',
        'to_do_2': 'Complete project',
        'to_do_3': 'Walk dog',
        'notes': 'Better finish project early!'
    }
]


def home(request):
    context = {
        'to_dos': to_do_list
    }
    return render(request, 'planner/home.html', context)


def calendar(request):
    return render(request, 'planner/calendar.html', {'title': 'Calendar'})
