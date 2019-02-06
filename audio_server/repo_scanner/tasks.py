import os
import time
from . import models
from celery import Celery
from django.utils.timezone import now
import custom_libs.wav_scan as wav_scan


app = Celery()

@app.task
def test_placeholder(num_iterations):
    for i in range(num_iterations):
        time.sleep(i)
        print("iteration number {}".format(i))


@app.task
def scan(target_path='/audio_repo'):

    for path, dirs, files in os.walk(target_path):
        for f in files:
            if f.endswith('.wav'):
                filepath = os.path.join(path, f)
                metadata = wav_scan.get_wav_metadata(filepath)


                same_asset = \
                        models.AudioAsset.objects.filter(filepath=filepath, crc=metadata['crc'])

                updated_asset = \
                        models.AudioAsset.objects.filter(filepath=filepath).exclude(crc=metadata['crc'])

                if same_asset:
                    continue

                elif updated_asset:
                    asset = updated_asset[0].update(scandate=now(),                                                              crc=metadata['crc'],
                                                    bitrate=metadata['bitrate'],
                                                    samplerate=metadata['samplerate'],
                                                    channels=metadata['channels'],
                                                    length=metadata['length'],
                                                    lufs=metadata['lufs'])
                else:
                    # new asset
                    models.AudioAsset.objects.create(filename=f,
                                                     filepath=filepath,
                                                     crc=metadata['crc'],
                                                     bitrate=metadata['bitrate'],
                                                     samplerate=metadata['samplerate'],
                                                     channels=metadata['channels'],
                                                     length=metadata['length'],
                                                     lufs=metadata['lufs'])