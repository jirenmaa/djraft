from django.db import models
from django.urls import reverse

from gdstorage.storage import GoogleDriveStorage

from djraft.users.models import User
from .utils import generate_slug

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()


class StoryManager(models.Manager):
    def only_uncover_article(self):
        """Return article without cover image."""

        return self.get_queryset().exclude(
            cover__regex='.', description__isnull=False
        )[:4]


# Create your models here.
class Story(models.Model):
    objects = StoryManager()
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, editable=False, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stories")

    cover = models.ImageField(blank=True, upload_to="cover", storage=gd_storage)
    description = models.TextField(blank=True, max_length=225)
    body = models.TextField(max_length=5500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at", "-updated_at"]
        permissions = (("do_something", "Do Something"),)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title, self.author.username)
        super().save(*args, **kwargs)

    @property
    def get_url_story_detail(self):
        return reverse(
            "users:article_detail",
            kwargs={"username": self.author.username, "slug": self.slug},
        )
