from django.forms import ModelForm
from .models import Article, Comment
from django import forms
from ckeditor.widgets import CKEditorWidget


class ArticleForm(ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = ["title", "content"]


class CommentForm(ModelForm):
    comment = forms.TextInput()

    class Meta:
        model = Comment
        fields = ["comment_content"]
