from django.shortcuts import render, render_to_response, HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from uploader import settings
from uploader import qqFileUploader
from uploader.models import Image

from uploader.tasks import process
import os
import json

def index(request):
    # show an upload button and a list of images.
    if request.method == 'POST':
        pass
    else:
        image_list = Image.objects.all()
        return render_to_response('uploader/index.html',  {'image_list': image_list})

@csrf_exempt
def upload(request):
    #uploader = qqFileUploader(request, os.path.join(settings.MEDIA_ROOT ,"upload/"), [".jpg", ".png", ".ico", ".*", ".avi"], 2147483648)
    uploader = qqFileUploader(request, settings.MEDIA_ROOT, [".jpg", ".png", ".ico", ".*", ".avi"], 2147483648)
    
    result = uploader.handleUpload() # returns, e.g. {'success': true}

    ##print type(file) # <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>

    # width and height will be set in postprocessing
    #image.width = image.image.width
    #image.height = image.image.height
    #image.title = "%s_%s" % (request.POST['qquuid'], request.POST['qqfilename'])

    # ONLY SAVE/PROCESS THIS IF THE UPLOAD HAS SUCCEEDED!
    d = json.loads(result) 
    if d['success'] == True:
        _file = request.FILES['qqfile'] # don't get this with S3?
        image = Image()
        image.uuid = request.POST['qquuid']
        image.save()
        taskresult = process.delay(image.uuid)

    return HttpResponse(result)

@csrf_exempt
def upload_delete(request, need_to_delete):
    qqFileUploader.deleteFile(need_to_delete)
    return HttpResponse("ok")


def image(request, image_id):
    image = Image.objects.get(id=image_id)
    return render_to_response('uploader/image.html',  {'image': image})
