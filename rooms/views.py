from django.utils import timezone
from django.views.generic import ListView
from django.shortcuts import render
from . import models

# Create your views here.


class HomeView(ListView):

    """HomeView Class Definition"""
    model = models.Room
    paginate_by = 10
    ordering = "created"
    paginate_orphans = 5
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now

        return context


def room_detail(request, pk):
    return render(request, "rooms/detail.html")
