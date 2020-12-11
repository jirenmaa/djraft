from django.urls import path

from djraft.users.views import (
    user_detail_view,
    user_update_view,
    user_story_detail_view,
    user_story_delete,
)

app_name = "users"
urlpatterns = [
    path("", view=user_detail_view, name="detail"),
    path("<slug:slug>", view=user_story_detail_view, name="article_detail"),
    path("<slug:slug>/delete", view=user_story_delete, name="article_delete"),
    path("~update", view=user_update_view, name="update"),
]
