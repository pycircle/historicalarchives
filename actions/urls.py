from django.conf.urls import patterns, url
from actions import views

urlpatterns = patterns('actions.views',
        url(r'^vote/(?P<pk>\d+)$', 'Vote', name = 'vote'),
        url(r'^actions$', 'ViewAllActions', name = 'actions'),
        url(r'^details/(?P<pk>\d+)$', 'DetailsOfAction', 'details'),
               )
