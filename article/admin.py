from .models import Article, Comment
from django.contrib import admin

# Register your models here.

@admin.register(Article)
class Articles(admin.ModelAdmin):
    list_display = ["title","author","date"]
    list_display_links = ["title", "author"]
    class Meta:
        model = Article

@admin.register(Comment)
class Comments(admin.ModelAdmin):
    list_display = ["commenter","comment_to","comment_date"]
    class Meta:
        model = Comment