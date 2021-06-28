from django.contrib import admin
from .models import Career

# Register your models here.


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ["owner", "firm", "advert_title", "advert_date"]
    list_display_links = ["owner", "advert_title"]

    class Meta:
        model = Career
