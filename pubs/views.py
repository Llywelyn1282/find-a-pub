from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Pub
from .forms import CommentForm


# Create your views here.
class PubList(generic.ListView):
    queryset = Pub.objects.filter(status=1)
    template_name = "pubs/index.html"
    paginate_by = 9


def pub_detail(request, slug):

    queryset = Pub.objects.filter(status=1)
    pub = get_object_or_404(queryset, slug=slug)
    comments = pub.comments.all().order_by("-created_on")
    comment_count = pub.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.pub = pub
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "pubs/pub_detail.html",
        {
            "pub": pub,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            },
    )
