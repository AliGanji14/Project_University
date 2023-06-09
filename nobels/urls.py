from django.urls import path

from .views import NobelListView

urlpatterns = [
    path("", NobelListView.as_view(), name="nobel_list"),

]
