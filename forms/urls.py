from django.contrib import admin
from django.urls import path, include
from forms import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.products.urls", namespace="products")),
    path("", include("apps.users.urls", namespace="users")),
]

if not settings.TESTING:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns = [*urlpatterns] + debug_toolbar_urls()
