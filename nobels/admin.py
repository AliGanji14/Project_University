from django.contrib import admin
from .models import Nobel, Comment


@admin.register(Nobel)
class AdminNobel(admin.ModelAdmin):
    list_display = ("user","name", "year", "country", "grouping", "datetime_created", "datetime_modified")


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ("user", "nobel", "text", "datetime_created","is_active")
