from django.shortcuts import render_to_response
from actions.models import Action

def Vote(request, pk):

    return render_to_response("actions/vote_page.html")

def DetailsOfAction(request, pk):
    action = Action.objects.get(pk = pk)
    return render_to_response("actions/action_detail.html", {'action': action})

def ViewAllActions(request):
    actions = Action.objects.all()
    return render_to_response("actions/actions_all.html", {'actions': actions})
