from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from recurrence.fields import RecurrenceField
from django.conf import settings
import datetime


def now_timestamp():
    return now().strftime("%Y-%m-%d %H:%M")

def default_scan_start_time():
    return now() + datetime.timedelta(minutes=5)

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

    scan_target_root = models.CharField(max_length=300, default='/audio_repo')
    scan_slug = models.CharField(max_length=100, default= str(now_timestamp()))
    scan_desc = models.CharField(max_length=500, default="Scan Started @ {}".format(now_timestamp()))
    scan_datetime = models.DateTimeField(default=default_scan_start_time)
    created_by = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete='cascade')

    def __str__(self):
        return "{}|{}|{}".format(self.created_by, self.scan_slug, self.scan_target_root)
