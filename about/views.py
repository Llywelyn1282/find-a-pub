from django.shortcuts import render
from django.views import generic
from .models import About


class About(generic.ListView):
    model = About
    template_name = "pubs/index.html"
