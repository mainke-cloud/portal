from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    menus = [
            {
                "title": "NDE", 
                "url": "https://new.coofis.com/api/auth/extoken",
                "icon": "fa-envelopes-bulk",
                "desc": "Aplikasi persuratan",
            },
            {
                "title": "Notes", 
                "url": "https://newnotes.coofis.com/oidc/authenticate",
                "icon": "fa-note-sticky",
                "desc": "Aplikasi untuk mencatat semua urusan anda",
            },
            {
                "title": "Reimburse", 
                "url": "https://newreimburse.coofis.com/oidc/authenticate",
                "icon": "fa-file-invoice",
                "desc": "Aplikasi untuk mencatat Reimburse anda",
            },
    ]
    return render(request, "index.html", locals())
