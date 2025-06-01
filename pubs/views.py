from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def my_pubs(request):
    return HttpResponse("This is the pub page.")