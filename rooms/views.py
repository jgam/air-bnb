from django.views.generic import ListView
from . import models

# Create your views here.


class HomeView(ListView):

    """HomeView Class Definition"""
    model = models.Room
    paginate_by = 10
    ordering = "created"
    paginate_orphans = 5
