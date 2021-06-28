from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.articles_page, name="articles_page"),
    path("dashboard/", views.dashboard_page, name="dashboard"),
    path("edit/", views.edit_article, name="edit_article"),
    path("detail/<int:id>/", views.article_detail, name="article_detail"),
    path("delete/<int:id>/", views.delete_article, name="article_delete"),
    path("update/<int:id>/", views.update_article, name="article_update"),
    path("ckeditor/", include("ckeditor_uploader.urls")),
]
