from django.shortcuts import render
from . import tasks
from . import models


def scan(request):
    template = 'repo_scanner/scan_home.html'
    result = tasks.scan.delay()
    return render(request, template)


def view_db(request):
    template = 'repo_scanner/view_db.html'
    audio_db = models.AudioAsset.objects.all()
    context = {'count':len(audio_db), 'audio_db':audio_db,}
    return render(request, template, context=context)