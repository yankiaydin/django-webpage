from .models import Profile, Architect, Constructor, Education
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="Username", max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(label="Email")

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        email = self.cleaned_data.get("email")
        values = {"username": username, "password": password, "email": email}
        return values


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["location", "web_page", "job", "bio", "profile_pic"]


class LoginForm(ModelForm):
    username = forms.CharField(label="Username", max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["username", "password"]


class myForm(forms.Form):
    username = forms.CharField(label="Username", max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        values = {"username": username, "password": password}
        return values


class ArchForm(forms.ModelForm):
    class Meta:
        model = Architect
        fields = ["office", "experience"]


class ConstForm(forms.ModelForm):
    class Meta:
        model = Constructor
        fields = ["company_name", "service"]


class EduForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ["university", "role"]
