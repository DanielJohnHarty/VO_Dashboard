from django.db import models

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
