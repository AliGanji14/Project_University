from django.urls import reverse_lazy
from django.views import generic

from .models import Nobel


class NobelListView(generic.ListView):
    model = Nobel
    template_name = "nobels/nobel_list.html"
    context_object_name = "nobels"


class NobelDetailView(generic.DetailView):
    model = Nobel
    template_name = "nobels/nobel_detail.html"


class NobelCreateView(generic.CreateView):
    model = Nobel
    fields = ["name", "description", "year", "country", "grouping","cover"]
    template_name = "nobels/nobel_create.html"


class NobelUpdateView(generic.UpdateView):
    model = Nobel
    fields = ["name", "description", "year", "country", "grouping","cover"]
    template_name = "nobels/nobel_update.html"


class NobelDeleteView(generic.DeleteView):
    model = Nobel
    template_name = "nobels/nobel_delete.html"
    success_url = reverse_lazy("nobel_list")
