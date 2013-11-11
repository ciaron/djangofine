from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'uploader.views.index', name='index'),
    url(r'^upload/$', 'uploader.views.upload', {}, 'upload'),
    url(r'^upload/(?P<need_to_delete>.*)$', "uploader.views.upload_delete", {}, 'upload_delete'),

)
