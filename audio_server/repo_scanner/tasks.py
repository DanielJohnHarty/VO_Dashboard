import os
from celery import Celery
import time

app = Celery()

@app.task
def test_placeholder(num_iterations):
    for i in range(num_iterations):
        time.sleep(i)
        print("iteration number {}".format(i))
