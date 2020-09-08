from django.urls import path

from obsidian.articles.views import (articles_view)

app_name = "articles"
urlpatterns = [
    path("", view=articles_view, name="articles"),
]
