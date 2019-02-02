import os
import time
from . import models
from celery import Celery

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
                asset = models.AudioAsset(filename=f, filepath=filepath)
                asset.save()