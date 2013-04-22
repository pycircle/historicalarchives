from django.shortcuts import render_to_response

def SearchForMaterial(request):
    return render_to_response('materials/materials_search.html')

def DetailsOfMaterials(request):
    return render_to_response("materials/material_details.html")

def AddMaterial(request):
    return render_to_response("materials/material_add.html")

def RequestMaterial(request):
    return render_to_response("materials/request_issue_new.html")

def ViewAllRequests(request):
    return render_to_response("materials/requests.html")

def DetailsOfRequest(request):
    return render_to_response("materials/request_details.html")
