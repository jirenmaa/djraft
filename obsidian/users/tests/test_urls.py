import pytest
from django.urls import resolve, reverse

from obsidian.users.models import User

pytestmark = pytest.mark.django_db


def test_detail(user: User):
    assert (
        reverse("users:detail", kwargs={"username": user.username})
        == f"/users/{user.username}/"
    )
    assert resolve(f"/users/{user.username}/").view_name == "users:detail"


def test_update():
    assert reverse("users:info") == "/users/~info/"
    assert resolve("/users/~info/").view_name == "users:info"


def test_redirect(user: User):
    assert reverse("users:redirect") == "/users/~redirect/"
    assert resolve("/users/~redirect/", kwargs={"username": user.username}).view_name == "users:redirect"
