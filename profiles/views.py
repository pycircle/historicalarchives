from django.template import RequestContext
from django.shortcuts import render_to_response

def Main(request):
    return render_to_response("profiles/account_page.html", context_instance=RequestContext(request))

def ViewAccount(request):
    return render_to_response("profiles/account_view.html", context_instance=RequestContext(request))

def ChangeSettings(request):
    return render_to_response("profiles/setup_view.html", context_instance=RequestContext(request))
