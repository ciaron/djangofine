from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'uploader.views.index', name='index'),
    url(r'^upload/$', 'uploader.views.upload', name='upload'),
    url(r'^upload/(?P<need_to_delete>.*)$', "uploader.views.upload_delete", name='upload_delete'),
    url(r'^image/(?P<image_id>\d+)/$', "uploader.views.image", name='image'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
#    # static files (images, css, javascript, etc.)
#    urlpatterns += patterns('django.contrib.staticfiles.views',
#        url(r'^upload/(?P<path>.*)$', 'serve', {
#        'document_root': settings.MEDIA_ROOT}))
