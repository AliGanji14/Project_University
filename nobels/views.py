from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Nobel
from .forms import CommentForm


class NobelListView(generic.ListView):
    model = Nobel
    paginate_by = 4
    template_name = "nobels/nobel_list.html"
    context_object_name = "nobels"


@login_required()
def nobe_detail_view(request, pk):
    # get nobel object
    nobel = get_object_or_404(Nobel, pk=pk)
    # get comment object
    nobel_comments = nobel.comments.all()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.nobel = nobel
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    return render(request, "nobels/nobel_detail.html", {
        "nobel": nobel,
        "comments": nobel_comments,
        "comment_form": comment_form,
    })


# class NobelDetailView(generic.DetailView):
#     model = Nobel
#     template_name = "nobels/nobel_detail.html"


class NobelCreateView(LoginRequiredMixin, generic.CreateView):
    model = Nobel
    fields = ["name", "description", "year", "country", "grouping", "cover"]
    template_name = "nobels/nobel_create.html"


class NobelUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Nobel
    fields = ["name", "description", "year", "country", "grouping", "cover"]
    template_name = "nobels/nobel_update.html"


class NobelDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Nobel
    template_name = "nobels/nobel_delete.html"
    success_url = reverse_lazy("nobel_list")
