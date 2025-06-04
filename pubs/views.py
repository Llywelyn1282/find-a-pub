from django.shortcuts import render
from django.views import generic
from .models import Pub

# Create your views here.
class PubList(generic.ListView):
    queryset = Pub.objects.filter(status=1)
    template_name = "pub_list.html"