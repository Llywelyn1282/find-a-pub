from django.shortcuts import render
from django.views import generic
from .models import About


# Create your views here.
class AboutList(generic.ListView):
    template_name = "about_list.html"
