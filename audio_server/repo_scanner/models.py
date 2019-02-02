from django.db import models

# Create your models here.
class AudioAsset(models.Model):
    filename = models.CharField(max_length=100)
    filepath = models.CharField(max_length=300)
