from django.shortcuts import render
from . import tasks
from . import models
from .forms import ScanTaskForm

def scan(request):
    template = 'repo_scanner/scan_home.html'
    # result = tasks.scan.delay()
    form = ScanTaskForm()
    context = {'form': form}
    return render(request, template, context)


def view_db(request):
    template = 'repo_scanner/view_db.html'
    audio_db = models.AudioAsset.objects.all()
    context = {'count':len(audio_db), 'audio_db':audio_db,}
    return render(request, template, context=context)