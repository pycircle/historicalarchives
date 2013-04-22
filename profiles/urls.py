from django.conf.urls import patterns, url

urlpatterns = patterns('profiles.views',
        url(r'^$', 'Main', name = 'main'),
        url(r'^view$', 'ViewAccount', name = 'view'),
        url(r'^settings$', 'ChangeSettings', name = 'settings'),
        )
