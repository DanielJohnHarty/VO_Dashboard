import os
from celery import Celery
import time

app = Celery('tasks', backend=os.environ['CELERY_BROKER_URL'], broker=os.environ['CELERY_BROKER_URL'])

@app.task
def test_placeholder(num_iterations):
    for i in range(num_iterations):
        time.sleep(i)
        print("iteration number {}".format(i))
