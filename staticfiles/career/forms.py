from django.forms import ModelForm
from .models import Career
from django import forms
from ckeditor.widgets import CKEditorWidget


class CareerForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Career
        fields = ["firm", "advert_title", "content"]
