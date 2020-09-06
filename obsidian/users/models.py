from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for Obsidian."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)

    # This field will be empty when the user
    # creates their account, so we specify `blank=True`.
    bio = models.TextField(blank=True)

    # Similar to `bio`, this field is not required. It may be blank.
    image = models.URLField(blank=True)

    # This is an example of a Many-To-Many relationship where both sides of the
    # relationship are of the same model. In this case, the model is `user`.
    # As mentioned in the text, this relationship will be one-way. Just because
    # you are following mean does not mean that I am following you. This is
    # what `symmetrical=False` does for us.
    follows = models.ManyToManyField(
        'self',
        related_name='followed_by',
        symmetrical=False
    )

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    def follow(self, user):
        """Follow `user` if we're not already following `user`."""
        self.follows.add(user)

    def unfollow(self, user):
        """Unfollow `user` if we're already following `user`."""
        self.follows.remove(user)

    def is_following(self, user):
        """Returns True if we're following `user`; False otherwise."""
        return self.follows.filter(pk=user.pk).exists()

    def is_followed_by(self, user):
        """Returns True if `user` is following us; False otherwise."""
        return self.followed_by.filter(pk=user.pk).exists()

