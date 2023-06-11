from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, render

from .models import Nobel


class NobelListView(generic.ListView):
    model = Nobel
    paginate_by = 4
    template_name = "nobels/nobel_list.html"
    context_object_name = "nobels"


def nobe_detail_view(request, pk):
    # get nobel object
    nobel = get_object_or_404(Nobel, pk=pk)

    # get comment object
    nobel_comments = nobel.comments.all()
    return render(request, "nobels/nobel_detail.html", {"nobel": nobel, "comments": nobel_comments})


# class NobelDetailView(generic.DetailView):
#     model = Nobel
#     template_name = "nobels/nobel_detail.html"


class NobelCreateView(generic.CreateView):
    model = Nobel
    fields = ["name", "description", "year", "country", "grouping", "cover"]
    template_name = "nobels/nobel_create.html"


class NobelUpdateView(generic.UpdateView):
    model = Nobel
    fields = ["name", "description", "year", "country", "grouping", "cover"]
    template_name = "nobels/nobel_update.html"


class NobelDeleteView(generic.DeleteView):
    model = Nobel
    template_name = "nobels/nobel_delete.html"
    success_url = reverse_lazy("nobel_list")
