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
    groups = [
                {"title": group.title, "slug": group.slug}
                for group in Group.objects.all()
             ]
    # ссылка в корень
    groups.insert(0, {"slug": "/", "title": "Посмотреть всё"})
    return render(request, "show_groups.html", {"groups": groups})


@login_required
def new_post(request):
    """  Создать новый пост"""
    if request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
            # Пользователь хранится в request.username
            # Данные формы после валидации лежат в form.cleaned_data['']
            post = Post(author=request.user,
                        text=form.cleaned_data['text'],
                        group=form.cleaned_data['group'])
            post.save()
            return redirect(reverse_lazy("index"))
    else:
        form = PostForm()
    return render(request, "new_post.html", {"form": form})
