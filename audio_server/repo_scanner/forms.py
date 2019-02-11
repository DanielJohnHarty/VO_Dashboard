from django.forms import forms, ModelForm
from .models import ScanTask
from bootstrap_datepicker_plus import DatePickerInput

class ScanTaskForm(ModelForm):
    class Meta:
        model = ScanTask
        fields = ('scan_target_root', 'scan_slug', 'scan_desc', 'scan_datetime')
        widgets = {'scan_datetime' : DatePickerInput(format='%Y-%m-%d %H:%M')}

