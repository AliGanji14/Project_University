from django.urls import path

from .views import NobelListView, NobelDetailView, NobelCreateView, NobelUpdateView, NobelDeleteView

urlpatterns = [
    path("", NobelListView.as_view(), name="nobel_list"),
    path("<int:pk>/", NobelDetailView.as_view(), name="nobel_detail"),
    path("new/", NobelCreateView.as_view(), name="nobel_create"),
    path("<int:pk>/edit/", NobelUpdateView.as_view(), name="nobel_update"),
    path("<int:pk>/delete/", NobelDeleteView.as_view(), name="nobel_delete"),

]
