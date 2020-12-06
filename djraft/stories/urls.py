from django.urls import path

from .views import (
    story_list_view,
    story_creation_view,
)

app_name = "stories"
urlpatterns = [
    path("stories", view=story_list_view, name="list"),
    path("new-story", view=story_creation_view, name="new-story"),
]
