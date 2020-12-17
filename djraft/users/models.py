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
    name = CharField(_("Name of User"), blank=True, max_length=255)
    about = TextField(_("About User"), default="Hi, I'm using Djraft.", max_length=255)
    #: user avatar
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
        if not self.avatar:
            getImg = get_default_avatar(self.username)
            self.avatar.save(getImg[0], getImg[1], save=True)

        super(User, self).save(*args, **kwargs)
