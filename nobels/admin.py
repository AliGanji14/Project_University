from django.contrib import admin
from .models import Nobel, Comment


@admin.register(Nobel)
class AdminBook(admin.ModelAdmin):
    list_display = ("name", "year", "country", "grouping", "datetime_created", "datetime_modified")


@admin.register(Comment)
class AdminBook(admin.ModelAdmin):
    list_display = ("user", "nobel", "text", "datetime_created","is_active")
