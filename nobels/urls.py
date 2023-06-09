from django.urls import path

from .views import NobelListView, NobelDetailView

urlpatterns = [
    path("", NobelListView.as_view(), name="nobel_list"),
    path("<int:pk>/", NobelDetailView.as_view(), name="nobel_detail"),

]
