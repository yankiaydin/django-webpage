from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "career"

urlpatterns = [
    path("", views.career_page, name="career_page"),
    path("advert/", views.career_advert, name="advert"),
    path("advert/<int:id>", views.advert_detail, name="advert_detail"),
]
