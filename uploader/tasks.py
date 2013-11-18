from __future__ import absolute_import
from subprocess import Popen
from PIL import Image
from celery import Celery
from django.conf import settings

import glob
import os
import mimetypes
import logging

from djangofine.celery import app
from .models import Image

@app.task()
def process(uuid):
    # add extra information to the database, like width and height
    image = Image.objects.get(uuid=uuid)
    image.width=69
    image.height=42
    image.save()
    #return "ProcessingDone"

@app.task()
def scale(uuid, size):

    #logger = logging.getLogger('imagequeue.tasks')
    #logger.setLevel(logging.INFO)
    #logger.addHandler(logging.StreamHandler())

    # beware! size might not be a key!
    sizes = {128: '_xxs', 256: '_xs', 500: '_s', 800: '_m', 1000: '_l', 1500: '_xl', 2000: '_xxl', 3000: '_xxxl'}

    if sizes.has_key(size):
        suffix = sizes[size]
    else:
        # make scaled image for next size down from 'size'
        i = 128
        for s in sorted(sizes.keys(), reverse=True): 
            if size > s:
                i = s
                break

        size = i
        suffix = sizes[size]

    file, ext = os.path.splitext(imagename)

    resizedname = imagename.replace(os.path.split(imagename)[0].split('/')[0], 'images')
    resizedfile, ext = os.path.splitext(resizedname)

    if mimetypes.guess_type(os.path.join(MEDIA_ROOT, imagename))[0] == 'image/tiff':
        ext = '.jpg'

    # do the image resizing with 'convert'
    # convert -resize 800x800 -auto-orient -quality 100 13176dcb-31f0-420a-a9f9-1ee91ebdf695.jpg test2.jpg
    outfile = os.path.join(MEDIA_ROOT, resizedfile + suffix + ext)

    if not os.path.exists(os.path.dirname(outfile)):
        try:
            os.makedirs(os.path.dirname(outfile))
        except OSError:
            pass
            #logger.info("Error: couldn't create %s" % os.path.dirname(outfile))

    logger.info("saving %s" % (outfile))
    args = ['/usr/bin/convert', '-resize', str(size)+'x'+str(size), '-auto-orient', '-quality', '90', os.path.join(MEDIA_ROOT, imagename), outfile]
    #logger.info("using command %s" % (args))

    p = Popen(args)
    p.wait()

    return "done"

@app.task()
def delete(imagename):

    original = imagename
    scaled = imagename.replace(os.path.split(imagename)[0].split('/')[0], 'images')

    scaledbase, scaledext = os.path.splitext(scaled)
    scaledwildcard = scaledbase + "*"

    # remove all generated images
    for f in glob.glob(os.path.join(MEDIA_ROOT, scaledwildcard)):
        os.remove(f)
    
    # remove original
    os.remove(os.path.join(MEDIA_ROOT, original))

    # TODO
    # remove from cache/ : or use a cronjob to clean cache?

    return "done delete"
