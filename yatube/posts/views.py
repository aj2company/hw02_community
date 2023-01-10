# posts/views.py
from django.shortcuts import render, get_object_or_404

from .models import Post, Group

POST_IN_PAGE = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()[:POST_IN_PAGE]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POST_IN_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
