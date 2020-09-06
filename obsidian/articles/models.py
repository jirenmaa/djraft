from django.db import models

from core.models import TimestampedModel
from users.models import User


class Tag(TimestampedModel):
    slug = models.SlugField(unique=True)
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag


class Article(TimestampedModel):
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=100)

    # Every article must have an author. This will answer questions like "Who
    # gets credit for writing this article?" and "Who can edit this article?".
    # Unlike the `User` <-> `Profile` relationship, this is a simple foreign
    # key (or one-to-many) relationship. In this case, one `Profile` can have
    # many `Article`s.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")

    description = models.TextField()
    body = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="articles")

    def __str__(self):
        return self.title


class Comments(TimestampedModel):
    body = models.TextField()

    # Comments are related to article that commented at
    article = models.ForeignKey(
        Article, related_name="comments", on_delete=models.CASCADE
    )

    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
