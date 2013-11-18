from django.shortcuts import render, render_to_response, HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from uploader import settings
from uploader import qqFileUploader
from uploader.models import Image

from uploader.tasks import process
import os

def index(request):
    # show an upload button and a list of images.
    if request.method == 'POST':
        pass
    else:
        image_list = Image.objects.all()
        return render_to_response('uploader/index.html',  {'image_list': image_list})

@csrf_exempt
def upload(request):
    uploader = qqFileUploader(request, os.path.join(settings.MEDIA_ROOT ,"upload/"), [".jpg", ".png", ".ico", ".*", ".avi"], 2147483648)
    
    result = uploader.handleUpload()

    # file is in request.POST (request.FILES?)
    # how do we know if handleUpload() has dealt with chunked or normal files?

    _file = request.FILES['qqfile'] # don't get this with S3?
    ##print type(file) # <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
    image = Image()
    image.uuid = request.POST['qquuid']

    # width and height will be set in postprocessing
    #image.width = image.image.width
    #image.height = image.image.height
    #image.title = "%s_%s" % (request.POST['qquuid'], request.POST['qqfilename'])
    image.save()
    taskresult = process.delay(image.uuid)

    return HttpResponse(result)

@csrf_exempt
def upload_delete(request, need_to_delete):
    qqFileUploader.deleteFile(need_to_delete)
    return HttpResponse("ok")


def image_detail(request):
    HttpResponse("not implemented yet")
