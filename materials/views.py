from django.shortcuts import render_to_response
from materials.models import Material, Request_for_materials, Collection

def SearchForMaterial(request):
    return render_to_response('materials/materials_search.html')

def DetailsOfMaterials(request, pk):
    material = Material.objects.get(pk = pk)
    return render_to_response("materials/material_details.html", {
        'material': material})

def AddMaterial(request):
    return render_to_response("materials/material_add.html")

def ViewNewMaterials(request):
    materials = Material.objects.all().order_by('date_of_creation')[:10]
    return render_to_response("materials/view_new_materials.html", {
        "materials": materials})

def RequestMaterial(request):
    return render_to_response("materials/request_issue_new.html")

def ViewAllRequests(request):
    requests = Request_for_materials.objects.all()
    return render_to_response("materials/requests.html", {
        'requests_list':requests})

def DetailsOfRequest(request, pk):
    request_for_materials = Request_for_materials.objects.get(pk = pk)
    return render_to_response("materials/request_details.html", {
        'request': request_for_materials})

def BuildCollection(request):
    return render_to_response("materials/collection_build.html")

def DetailsOfCollection(request, pk):
    collection =Collection.objects.get(pk = pk)
    return render_to_response("materials/collection_details.html", {
        "collection": collection})

def ViewAllCollections(request):
    collections = Collection.objects.all()
    return render_to_response("materials/collections.html", {
        "collections": collections})
