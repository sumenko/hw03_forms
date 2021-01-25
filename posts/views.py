from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .models import Post, Group
from .forms import PostForm


def index(request):
    """ Вывод последних 10 постов из базы """
    latest = Post.objects.all()[:10]
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug=None):
    # Получаем объект из базы соответствующий slug
    group = get_object_or_404(Group, slug=slug)
    # Получаем все посты принадлежащие slug через related_name
    posts = group.posts.all()[:12]
    return render(request, "group.html", {"group": group, "posts": posts})


def show_groups(request):
    """ Показывает страницу со списком всех сообществ """
    groups = Group.objects.all()[:10]
    return render(request, "show_groups.html", {"groups": groups})


@login_required
def new_post(request):
    """ Создать новый пост """
    form = PostForm(request.POST or None)

    if request.GET or not form.is_valid():
        return render(request, "new_post.html", {"form": form})

    post = form.save(commit=False)
    post.author = request.user
    post.save()

    return redirect(reverse_lazy("index"))
