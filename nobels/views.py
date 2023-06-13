from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Nobel
from .forms import NobelForm, CommentForm


def nobel_list_view(request):
    if "q" in request.GET:
        q = request.GET["q"]
        nobels = Nobel.objects.filter(name__icontains=q)
    else:
        nobels = Nobel.objects.all().order_by("-datetime_created")
    paginator = Paginator(nobels, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "nobels": page_obj,
    }
    return render(request, "nobels/nobel_list.html", context)


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


@login_required()
def nobel_create_view(request):
    if request.method == "POST":
        create_nobel = NobelForm(request.POST)
        if create_nobel.is_valid():
            new_nobel = create_nobel.save(commit=False)
            new_nobel.user = request.user
            new_nobel.save()
            return redirect(new_nobel)
    else:
        create_nobel = NobelForm()
    return render(request, "nobels/nobel_create.html", {"form": create_nobel})


class NobelUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Nobel
    fields = ["name", "description", "year", "country", "grouping", "cover"]
    template_name = "nobels/nobel_update.html"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class NobelDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Nobel
    template_name = "nobels/nobel_delete.html"
    success_url = reverse_lazy("nobel_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
