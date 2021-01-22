from django.urls import path
from . import views

# у нас два варианта: вывод всех постов или по сообществу
urlpatterns = [
    path("", views.index, name="index"),
    path("group/<slug:slug>/", views.group_posts, name="group-slug"),
]
