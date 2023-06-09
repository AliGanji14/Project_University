from django.urls import reverse_lazy
from django.views import generic

from .models import Nobel


class NobelListView(generic.ListView):
    model = Nobel
    template_name = "nobels/nobel_list_view.html"
    context_object_name = "nobels"


class NobelDetailView(generic.DetailView):
    model = Nobel
    template_name = "nobels/nobel_detail_view.html"


class NobelCreateView(generic.CreateView):
    model = Nobel
    fields = ["name", "description", "year", "country", "grouping"]
    template_name = "nobels/nobel_create_view.html"


class NobelUpdateView(generic.UpdateView):
    model = Nobel
    fields = ["name", "description", "year", "country", "grouping"]
    template_name = "nobels/nobel_update_view.html"


class NobelDeleteView(generic.DeleteView):
    model = Nobel
    template_name = "nobels/nobel_delete_view.html"
    success_url = reverse_lazy("nobel_list")
