from django.shortcuts import render
from . import tasks


def scan_home(request):
    template = 'repo_scanner/scan_home.html'
    context = {}

    # Create an async task. Status visible @ localhost:5555
    result = tasks.test_placeholder.delay(5)
    return render(request, template, context=context)