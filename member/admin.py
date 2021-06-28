from django.contrib import admin
from .models import Profile, Architect, Constructor, Education

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "location", "web_page", "job"]

    class Meta:
        model = Profile


@admin.register(Architect)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "office", "experience"]

    class Meta:
        model = Architect


@admin.register(Constructor)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "company_name", "service"]

    class Meta:
        model = Constructor


@admin.register(Education)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "university", "role"]

    class Meta:
        model = Education
