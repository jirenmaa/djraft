from django.urls import path
from django.views.generic import TemplateView

from obsidian.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    user_stories_view,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("", view=user_detail_view, name="detail"),
    path("stories/", view=user_stories_view, name="stories")
]
