from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'python_django_s3.views.home', name='home'),
    # url(r'^python_django_s3/', include('python_django_s3.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 's3uploader.views.home', name='home'),
    url(r'^signature', 's3uploader.views.handle_s3', name="s3_signee"),
    url(r'^delete', 's3uploader.views.handle_s3', name='s3_delete'),
    url(r'^success', 's3uploader.views.success_redirect_endpoint', name="s3_success_endpoint")
)

