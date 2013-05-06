from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'historicalarchives.views.Index', name = 'index'),
    url(r'^actions/', include('actions.urls', namespace="actions")),
    url(r'^materials/', include('materials.urls', namespace="materials")),
    url(r'^other_tags/', include('other_tags.urls', namespace="other_tags")),
    url(r'^profiles/', include('profiles.urls', namespace="profiles")),
    url(r'^timeline/', include('timeline.urls', namespace="timeline")),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATICFILES_DIRS[0], 'show_indexes':True}),
    )
