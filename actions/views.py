from django.shortcuts import render_to_response

def Vote(request):
    return render_to_response("actions/vote_page.html")
