from django.template import RequestContext
from django.shortcuts import render_to_response

def SearchForMaterial(request):
    return render_to_response('materials/materials_search.html', context_instance=RequestContext(request))

def DetailsOfMaterials(request):
    return render_to_response("materials/material_details.html", context_instance=RequestContext(request))

def AddMaterial(request):
    return render_to_response("materials/material_add.html", context_instance=RequestContext(request))

def RequestMaterial(request):
    return render_to_response("materials/request_issue_new.html", context_instance=RequestContext(request))

def ViewAllRequests(request):
    return render_to_response("materials/requests.html", context_instance=RequestContext(request))

def DetailsOfRequest(request):
    return render_to_response("materials/request_details.html", context_instance=RequestContext(request))

def BuildCollection(request):
    return render_to_response("materials/collection_build.html", context_instance=RequestContext(request))

def DetailsOfCollection(request):
    return render_to_response("materials/collection_details.html", context_instance=RequestContext(request))

def ViewAllCollections(request):
    return render_to_response("materials/collections.html", context_instance=RequestContext(request))
