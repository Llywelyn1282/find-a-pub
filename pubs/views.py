from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Pub, Comment
from .forms import CommentForm


# Create your views here.

# Home Page
class PubList(generic.ListView):
    queryset = Pub.objects.filter(status=1).order_by("?")
    template_name = "pubs/index.html"


# Filters
def pub_filtered_list(request):
    pubs = Pub.objects.filter(status=1)
    filter_list = request.GET.get('filters', '')
    filters = filter_list.split(',') if filter_list else []

    if 'food' in filters:
        pubs = pubs.filter(food="Yes")
    if 'craft_beer' in filters:
        pubs = pubs.filter(craft_beer="Yes")
    if 'beer_garden' in filters:
        pubs = pubs.filter(beer_garden="Yes")
    if 'dog_friendly' in filters:
        pubs = pubs.filter(dog_friendly="Yes")
    if 'pool_table' in filters:
        pubs = pubs.filter(pool_table="Yes")
    if 'dart_board' in filters:
        pubs = pubs.filter(dart_board="Yes")

    return render(request, "pubs/index.html", {"pub_list": pubs})


# Pub Detail Page
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


# Comment Edit
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
            messages.add_message(request,
                                 messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('pub_detail', args=[slug]))


# Comment Delete
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
