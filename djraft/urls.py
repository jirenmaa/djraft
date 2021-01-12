from django.urls import path

from djraft.users.views import user_settings_view
from djraft.stories.views import (
    story_list_view,
    story_creation_view,
    story_update_view,
    story_delete_view,
)


app_name = "djraft"
urlpatterns = [
    # users app
    path("settings/", view=user_settings_view, name="settings"),
    # stories app
    path("stories/", view=story_list_view, name="stories"),
    path("new-story/", view=story_creation_view, name="new_story"),
    path("<slug:slug>/edit", view=story_update_view, name="edit_story"),
    path("<str:slug>/delete", view=story_delete_view, name="delete_story"),
    # others app
]
