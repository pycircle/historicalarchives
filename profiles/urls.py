from django.conf.urls import patterns, url
from profiles import views

urlpatterns = patterns('profiles.views',
        url(r'^$', 'Main', name = 'main'),
        url(r'^view$', 'ViewAccount', name = 'view'),
        url(r'^settings$', 'ChangeSettings', name = 'settings'),
        )
