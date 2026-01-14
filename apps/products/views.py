from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from apps.products.forms import TagForm
from apps.products.models import Tag


def create_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)

        # print(form.errors)
        # print(form.is_valid())
        # print(form.cleaned_data)
        # print(form.as_table())
        # print(form.base_fields["name"].label)
        # print(form.fields["name"].label)
        # print(form.get_context())
        # print("data", form.data)
        # form.is_valid()
        # print("cleaned_data", form.cleaned_data)
        # print(form.template_name)

        # print(dir(form))



        if form.is_valid():
            # form.save()
            return HttpResponse("Tag was created successfully")
            return HttpResponseRedirect(reverse("products:tag-list"))
    form = TagForm()
    return render(request, "products/tag_form.html", context={"form": form})


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
