from django.shortcuts import render, render_to_response, HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from uploader import settings
from uploader import qqFileUploader
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
    return HttpResponse(uploader.handleUpload())

@csrf_exempt
def upload_delete(request, need_to_delete):

    qqFileUploader.deleteFile(need_to_delete)

    return HttpResponse("ok")

