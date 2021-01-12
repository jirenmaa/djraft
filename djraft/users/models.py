from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, TextField, ImageField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from gdstorage.storage import GoogleDriveStorage

from .helper import get_default_avatar

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()


class User(AbstractUser):
    """Default user for djraft."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=100)
    bio = TextField(_("UserBio"), default="Hi, there.", max_length=160)
    # user avatar
    avatar = ImageField(
        upload_to="avatar",
        storage=gd_storage,
    )

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    def save(self, *args, **kwargs):
        self.username = self.username[0].upper() + self.username[1:]

        if not self.avatar:
            get_img = get_default_avatar(self.username)
            self.avatar.save(get_img[0], get_img[1], save=True)

        super(User, self).save(*args, **kwargs)
