from django.db import models
from django.utils import timezone
from random import randint

from djraft.users.models import User
from .utils import generate_slug


class StoryManager(models.Manager):
    def get_excover_queryset(self):
        return self.get_queryset().exclude(cover='')

    def random(self, queryset):
        count = queryset.count()
        random_index = randint(0, count - 1)
        return queryset[random_index]


class Story(models.Model):
    objects = StoryManager()
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=100)

    # Every article must have an author. This will answer questions like "Who
    # gets credit for writing this article?" and "Who can edit this article?".
    # Unlike the `User` <-> `Profile` relationship, this is a simple foreign
    # key (or one-to-many) relationship. In this case, one `Profile` can have
    # many `Article`s.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stories")

    cover = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at", "-updated_at"]

    def __str__(self):
        return self.title

    def save(self):
        self.slug = generate_slug(self.title, timezone.now())
        super(Story, self).save()
