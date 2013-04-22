from django.shortcuts import render_to_response

def Main(request):
    return render_to_response("profiles/account_page.html")

def ViewAccount(request):
    return render_to_response("profiles/account_view.html")

def ChangeSettings(request):
    return render_to_response("profiles/setup_view.html")
