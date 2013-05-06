from django.template import RequestContext
from django.shortcuts import render_to_response
from materials.models import Material, Request_for_materials, Collection

def SearchForMaterial(request):
    return render_to_response('materials/materials_search.html', context_instance=RequestContext(request))

def DetailsOfMaterials(request, pk):
    material = Material.objects.get(pk = pk)
    return render_to_response("materials/material_details.html", {
        'material': material}, context_instance=RequestContext(request))

def AddMaterial(request):
    return render_to_response("materials/material_add.html", context_instance=RequestContext(request))

def ViewNewMaterials(request):
    materials = Material.objects.all().order_by('date_of_creation')[:10]
    return render_to_response("materials/view_new_materials.html", {
        "materials": materials}, context_instance=RequestContext(request))

def RequestMaterial(request):
    return render_to_response("materials/request_issue_new.html", context_instance=RequestContext(request))

def ViewAllRequests(request):
    requests = Request_for_materials.objects.all()
    return render_to_response("materials/requests.html", {
        'requests_list':requests}, context_instance=RequestContext(request))

def DetailsOfRequest(request, pk):
    request_for_materials = Request_for_materials.objects.get(pk = pk)
    return render_to_response("materials/request_details.html", {
        'request': request_for_materials}, context_instance=RequestContext(request))

def BuildCollection(request):
    return render_to_response("materials/collection_build.html", context_instance=RequestContext(request))

def DetailsOfCollection(request, pk):
    collection =Collection.objects.get(pk = pk)
    return render_to_response("materials/collection_details.html", {
        "collection": collection}, context_instance=RequestContext(request))

def ViewAllCollections(request):
    collections = Collection.objects.all()
    return render_to_response("materials/collections.html", {
        "collections": collections}, context_instance=RequestContext(request))
