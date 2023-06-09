from django.views import generic
from .models import Nobel


class NobelListView(generic.ListView):
    model = Nobel
    template_name = "nobels/nobel_list_view.html"
    context_object_name = "nobels"


class NobelDetailView(generic.DetailView):
    model = Nobel
    template_name = "nobels/nobel_detail_view.html"
