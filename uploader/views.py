from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
    #return HttpResponse("hey!")
    if request.method == 'POST':
        pass
    else:
        return render(request, 'uploader/index.html', )
