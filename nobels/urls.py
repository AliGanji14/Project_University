from django.urls import path

from .views import NobelListView, NobelDetailView, NobelCreateView

urlpatterns = [
    path("", NobelListView.as_view(), name="nobel_list"),
    path("<int:pk>/", NobelDetailView.as_view(), name="nobel_detail"),
    path("new/", NobelCreateView.as_view(), name="nobel_create")

]
