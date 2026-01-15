from django import forms
from apps.products.models import Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"


class TagUnboundedForm(forms.Form):
    name = forms.CharField(initial="www", label="Name))))", widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    slug = forms.CharField(max_length=1, label="Slug", empty_value="9", required=False)
