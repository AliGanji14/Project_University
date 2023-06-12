from django.urls import path

from .views import nobel_list_view, nobe_detail_view, NobelCreateView, NobelUpdateView, NobelDeleteView

urlpatterns = [
    path("", nobel_list_view, name="nobel_list"),
    path("<int:pk>/", nobe_detail_view, name="nobel_detail"),
    path("new/", NobelCreateView.as_view(), name="nobel_create"),
    path("<int:pk>/edit/", NobelUpdateView.as_view(), name="nobel_update"),
    path("<int:pk>/delete/", NobelDeleteView.as_view(), name="nobel_delete"),

]
