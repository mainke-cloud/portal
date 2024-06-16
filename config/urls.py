from django.contrib import admin
from django.urls import path, include
from portal.views import index

urlpatterns = [
    path("",index, name="portal-index"),
    path('oidc/', include('mozilla_django_oidc.urls')),
    path('admin/', admin.site.urls),
]
