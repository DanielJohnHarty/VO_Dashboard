from django.shortcuts import render
from . import tasks
from . import models
from .forms import ScanTaskForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.timezone import now


'''
now() + datetime.timedelta(hours=1) #1 hour ahead  
'''

def scan(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ScanTaskForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            target_path = form.cleaned_data['scan_root']
            execution_datetime = form.cleaned_data['scan_datetime']
            result = tasks.scan.apply_async(target_path=target_path, eta=execution_datetime)

            #result = tasks.scan.delay(target_path=target_path)
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('home'))

    # if a GET (or any other method) we'll create a blank form
    else:

        template = 'repo_scanner/scan_home.html'
        form = ScanTaskForm()
        context = {'form': form}
        return render(request, template, context)












def view_db(request):
    template = 'repo_scanner/view_db.html'
    audio_db = models.AudioAsset.objects.all()
    context = {'count':len(audio_db), 'audio_db':audio_db,}
    return render(request, template, context=context)