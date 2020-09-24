from django.urls import path

from obsidian.articles.views import articles_list_view, articles_create_view

app_name = "articles"
urlpatterns = [
    path("", view=articles_list_view, name="articles"),
    path("~write/", view=articles_create_view, name="write"),
]
