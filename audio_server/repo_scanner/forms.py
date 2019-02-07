from django.forms import forms, ModelForm, FilePathField
from .models import ScanTask

class ScanTaskForm(ModelForm):
    class Meta:
        model = ScanTask
        #fields = ['pub_date', 'headline', 'content', 'reporter']
        fields = ('scan_root', 'scan_slug', 'scan_desc')
        # widgets = {
        #     'scan_root': FilePathField('/'),
        # }
