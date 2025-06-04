from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Pub

# Create your views here.
class PubList(generic.ListView):
    queryset = Pub.objects.filter(status=1)
    template_name = "pubs/index.html"
    paginate_by = 9

def pub_detail(request, slug):
    
    queryset = Pub.objects.filter(status=1)
    pub = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "pubs/pub_detail.html",
        {"pub": pub},
    )