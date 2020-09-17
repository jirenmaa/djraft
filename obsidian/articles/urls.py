from django.urls import path

from obsidian.articles.views import (articles_view, articles_create)

app_name = "articles"
urlpatterns = [
    path("", view=articles_view, name="articles"),
    path("~create/", view=articles_create, name="create"),
    # path("@<str:username>/<str:title_slug>")
]
