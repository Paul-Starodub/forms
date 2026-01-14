from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from apps.products.models import Tag


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("products:tag-list")


class TagDetailView(LoginRequiredMixin, generic.DetailView):
    model = Tag


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    paginate_by = 20


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("products:tag-list")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("products:tag-list")
