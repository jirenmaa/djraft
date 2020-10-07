from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for obsidian."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)

    # This field is not required. It may be blank.
    avatar = models.ImageField(blank=True)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    def delete_old_avatar(user):
        # You have to prepare what you need before delete the model
        storage, path = user.avatar.storage, user.avatar.path
        # Delete the model before the file
        super(User, user).delete()
        # Delete the file after the model
        storage.delete(path)
