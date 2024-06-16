from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    menus = [
            {"title": "NDE", "url": "https://new.coofis.com/api/auth/extoken"},
            {"title": "Notes", "url": "https://newnotes.coofis.com/oidc/authenticate"},
    ]
    return render(request, "index.html", locals())
