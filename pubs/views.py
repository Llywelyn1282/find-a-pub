from django.shortcuts import render
from django.views import generic
from .models import Pub

# Create your views here.
class PubList(generic.ListView):
    model = Pub