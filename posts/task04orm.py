from django.shortcuts import render
from .models import Post, User
from datetime import date


def index(request):
    author = User.objects.get(username="leo")
    keyword = "утро"
    posts = Post.objects.filter(
            author=author,
            pub_date__date__range=(date(1854, 7, 7), date(1854, 7, 21)),
            text__contains=keyword
            )
    return render(request, "index.html", {"posts": posts})
