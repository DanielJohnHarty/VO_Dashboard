from django.db import models
from django.contrib.auth.models import User
from recurrence.fields import RecurrenceField
from django.conf import settings

# Create your models here.
class AudioAsset(models.Model):
    filename = models.CharField(max_length=100)
    filepath = models.CharField(max_length=300)
    scandate = models.DateTimeField(auto_now=True)
    bitrate = models.IntegerField(null=True)
    length = models.FloatField(null=True)
    samplerate = models.IntegerField(null=True)
    lufs = models.FloatField(null=True)
    channels = models.IntegerField(null=True)
    crc = models.CharField(null=True, max_length=100)

    def __str__(self):
        return "{}_{}".format(self.filename, self.crc)

class ScanTask(models.Model):
    scan_root = models.CharField(max_length=300)
    scan_slug = models.CharField(max_length=100)
    scan_desc = models.CharField(max_length=500)
    recurrence = RecurrenceField()
    active = models.BooleanField(default=True)
    created_by = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete='cascade')