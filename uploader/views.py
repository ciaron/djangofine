from django.shortcuts import render, render_to_response, HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from uploader import settings
from uploader import qqFileUploader
from uploader.models import Image

import os

def index(request):
    #return HttpResponse("hey!")
    if request.method == 'POST':
        pass
    else:
        return render(request, 'uploader/index.html', )

@csrf_exempt
def upload(request):
    uploader = qqFileUploader(request, os.path.join(settings.MEDIA_ROOT ,"upload/"), [".jpg", ".png", ".ico", ".*", ".avi"], 2147483648)
    
    result = uploader.handleUpload()

    # file is in request.POST (request.FILES?)
    # how do we know if handleUpload() has dealt with chunked or normal files?

    file = request.FILES['qqfile']
    image = Image()
    image.image = file
    image.width = image.image.width
    image.height = image.image.height
    image.title = "%s_%s" % (request.POST['qquuid'], request.POST['qqfilename'])
    image.save()

    return HttpResponse(result)

@csrf_exempt
def upload_delete(request, need_to_delete):

    qqFileUploader.deleteFile(need_to_delete)

    return HttpResponse("ok")

