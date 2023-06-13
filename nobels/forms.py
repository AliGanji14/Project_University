from django import forms
from .models import Nobel, Comment


class NobelForm(forms.ModelForm):
    class Meta:
        model = Nobel
        fields = ("name", "description", "year", "country", "grouping", "cover",)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
