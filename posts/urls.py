from django.urls import path

from . import views

# у нас два варианта: вывод всех постов или по сообществу
urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new_post, name="new_post"),
    path("group/<slug:slug>/", views.group_posts, name="group-slug"),
    path("group/", views.show_groups, name="show_groups"),
]
