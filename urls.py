from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from matthewdhowell.pushy_articulator.views import index

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^matthewdhowell/', include('matthewdhowell.foo.urls')),
    (r'^$', index),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Static site media. FIXME in production this should be served by the
    # main web server or other service.  There's no reason to lug that
    # data through Django.
    (
        r'^site_media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.STATIC_DOC_ROOT},
    ),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
