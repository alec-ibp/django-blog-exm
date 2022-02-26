from .models import Category
from .models import Post

from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator


def home(request):
    queryset = request.GET.get("search")

    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains = queryset) |
            Q(description__icontains = queryset),
            status = True
        ).distinct()

    else:
        posts = Post.objects.filter(status = True)

    paginator = Paginator(posts, 1)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    return render(request, "index.html", {"posts": posts})


def detail_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "post.html", {"post": post})


def general(request):
    queryset = request.GET.get("search")

    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains = queryset) |
            Q(description__icontains = queryset),
            status = True,
            category = Category.objects.get(name__iexact = "General")
        ).distinct()

    else:
        posts = Post.objects.filter(
            status = True,
            category = Category.objects.get(name__iexact = "General")
        )

    return render(request, "general.html", {"posts": posts})


def technology(request):
    posts = Post.objects.filter(
        status = True,
        category = Category.objects.get(name__iexact = "Technology")
    )
    return render(request, "technology.html", {"posts": posts})


def tutorials(request):
    return render(request, "tutorials.html")


def contact(request):
    return render(request, "contact.html")