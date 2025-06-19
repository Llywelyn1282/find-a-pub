from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Pub, Comment
from .forms import CommentForm


# Create your views here.
class PubList(generic.ListView):
    queryset = Pub.objects.filter(status=1).order_by("?")
    template_name = "pubs/index.html"
    paginate_by = 6


def pub_list(request):
    filters = request.GET.get('filters')
    pubs = Pub.objects.all()
    filter_list = []

    if filters:
        filter_list = filters.split(',')

        for f in filter_list:
            if f == "food":
                pubs = pubs.filter(food="Yes")
            elif f == "craft_beer":
                pubs = pubs.filter(craft_beer="Yes")
            elif f == "beer_garden":
                pubs = pubs.filter(beer_garden="Yes")
            elif f == "dog_friendly":
                pubs = pubs.filter(dog_friendly="Yes")
            elif f == "pool_table":
                pubs = pubs.filter(pool_table="Yes")
            elif f == "dart_board":
                pubs = pubs.filter(dart_board="Yes")

    return render(request, "pub_list.html", {
        "pubs": pubs,
        "selected_filters": filter_list,
    })


def pub_detail(request, slug):

    queryset = Pub.objects.filter(status=1)
    pub = get_object_or_404(queryset, slug=slug)
    comments = pub.comments.all().order_by("-created_on")
    comment_count = pub.comments.count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.pub = pub
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted successfully!'
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


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Pub.objects.filter(status=1)
        pub = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.pub = pub
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('pub_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Pub.objects.filter(status=1)
    pub = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message
        (request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('pub_detail', args=[slug]))
