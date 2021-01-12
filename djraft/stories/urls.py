from django.urls import path

from djraft.stories.views import (
    like,
    dislike
)

app_name = "stories"
urlpatterns = [
    path("like/<int:_id>", view=like, name="like"),
    path("dislike/<int:_id>", view=dislike, name="dislike"),
]
