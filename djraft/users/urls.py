from django.urls import path

from .views import (
    user_detail_view,
    user_redirect_view,
    user_info_view,
    user_stories_view,
    user_story_detail_view,
    user_story_delete,
    user_story_edit_view,
    user_new_stories_view,
)

app_name = "users"
urlpatterns = [
    # user related account
    path("", view=user_detail_view, name="detail"),
    path("~redirect", view=user_redirect_view, name="redirect"),
    path("~info", view=user_info_view, name="info"),
    # user related story or article
    path("~stories", view=user_stories_view, name="stories"),
    path("<slug:slug>", view=user_story_detail_view, name="story"),
    path("<slug:slug>/delete", view=user_story_delete, name="delete"),
    path("<slug:slug>/edit", view=user_story_edit_view, name="edit"),
    path("~new-story", view=user_new_stories_view, name="new-story"),
]
