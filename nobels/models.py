from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model


class Nobel(models.Model):
    STATUS_CHOICES = (
        ('chemistry', 'chemistry'),
        ('economy', 'economy'),
        ("literature", "literature"),
        ("nobel peace", "nobel peace"),
        ("physics", "physics"),
        ("physiology and medicine", "physiology and medicine"),
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    year = models.PositiveIntegerField()
    country = models.CharField(max_length=50)
    grouping = models.CharField(choices=STATUS_CHOICES, max_length=23)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("nobel_detail", args=[self.id])
