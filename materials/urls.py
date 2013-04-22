from django.conf.urls import patterns, url
from materials import views

urlpatterns = patterns('materials.views',
        url(r'^search$', 'SearchForMaterial', name = 'search'),
        url(r'^details$', 'DetailsOfMaterials', name = 'details'),
        url(r'^add$', 'AddMaterial', name = 'add'),
        url(r'^request_add$', 'RequestMaterial', name = 'request_add'),
        url(r'^requests$', 'ViewAllRequests', name = 'requsets'),
        url(r'^request_details$', 'DetailsOfRequest', name = 'reqeust_detail'),
        )
