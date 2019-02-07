from django.http import HttpResponseRedirect


def tasks(request):
    return HttpResponseRedirect('http://localhost:5555/tasks')