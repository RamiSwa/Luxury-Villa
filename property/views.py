from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Property 

# Create your views here.

class PropertyList(ListView):
    model = Property

    # filter
    # pagination


class PropertyDetail(DetailView):
    model = Property

    # filter
    # book