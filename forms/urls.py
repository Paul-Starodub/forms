from django.contrib import admin
from django.urls import path
from forms import settings

urlpatterns = [
    path("admin/", admin.site.urls),
]

if not settings.TESTING:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns = [*urlpatterns] + debug_toolbar_urls()
