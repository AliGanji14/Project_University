from django.contrib import admin
from .models import Nobel


@admin.register(Nobel)
class AdminBook(admin.ModelAdmin):
    list_display = ("name", "year", "country","grouping","datetime_created","datetime_modified")

