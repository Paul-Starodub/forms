from django.urls import path
from apps.products.views import TagCreateView, TagListView, TagDetailView, TagUpdateView, TagDeleteView

app_name = "products"


urlpatterns = [
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<int:pk>/", TagDetailView.as_view(), name="tag-detail"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="task-type-delete"),
]
