from django.conf.urls import patterns, url

urlpatterns = patterns('materials.views',
        url(r'^search$', 'SearchForMaterial', name = 'search'),
        url(r'^details/(?P<pk>\d+)$', 'DetailsOfMaterials', name = 'details'),
        url(r'^add$', 'AddMaterial', name = 'add'),
        url(r'^viewnew$', 'ViewNewMaterials', name = 'viewnew'),
        url(r'^request_add$', 'RequestMaterial', name = 'request_add'),
        url(r'^requests$', 'ViewAllRequests', name = 'requests'),
        url(r'^request_details/(?P<pk>\d+)$', 'DetailsOfRequest', name = 'reqeust_detail'),
        url(r'^collection_build$'/(?P<pk>\d+), 'BuildCollection', name='collection_build'),
        url(r'^collection_details$', 'DetailsOfCollection', name='collection_details'),
        url(r'^collections$', 'ViewAllCollections', name='collections'),
        )
