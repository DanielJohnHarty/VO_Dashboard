from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import tasks
from . import models
from .forms import ScanTaskForm
import custom_libs.nas_mount_utils as nmu


def scan(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ScanTaskForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # Save the ScanTask to the db
            new_scantask = models.ScanTask(**form.cleaned_data, created_by=request.user)
            new_scantask.save()
            
            # Create the celery scan task
            passed_scan_target = form.cleaned_data['scan_target_root']
            server_path = nmu.return_server_filepath_if_exists(passed_scan_target)

            if server_path:
                execution_datetime = form.cleaned_data['scan_datetime']
                result = tasks.scan.apply_async([server_path], eta=execution_datetime)

                # redirect home if successful:
                return HttpResponseRedirect(reverse('home'))
            else:
                # Reload page if unsuccessful (must add error message dialog)
                return HttpResponseRedirect(reverse('repo_scanner:scan'))


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