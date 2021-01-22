from django.shortcuts import render, get_object_or_404

from .models import Post, Group


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
