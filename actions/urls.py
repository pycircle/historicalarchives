from django.conf.urls import patterns, url
from actions import views

urlpatterns = patterns('actions.views',
        url(r'^$', 'Vote', name = 'vote'),
               )
