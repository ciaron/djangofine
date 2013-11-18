from __future__ import absolute_import
from subprocess import Popen
from PIL import Image
from celery import Celery
from django.conf import settings

import glob
import os
import mimetypes
import logging

#from uploader import Image

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangofine.settings')

app = Celery('djangofine',
             broker='amqp://',
             backend='amqp://',
             include=['uploader.tasks'])

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(settings.INSTALLED_APPS, related_name='tasks')

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

