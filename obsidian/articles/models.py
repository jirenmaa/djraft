from django.db import models
from django.db.models import Count
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

from random import randint

from core.models import TimestampedModel
from obsidian.users.models import User


class Tag(TimestampedModel):
    slug = models.SlugField(unique=True)
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag


class ArticleManager(models.Manager):
    def random(self):
        count = self.aggregate(ids=Count("id"))["ids"]
        random_index = randint(0, count - 1)
        return self.all()[random_index]


class Article(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=100)

    # Every article must have an author. This will answer questions like "Who
    # gets credit for writing this article?" and "Who can edit this article?".
    # Unlike the `User` <-> `Profile` relationship, this is a simple foreign
    # key (or one-to-many) relationship. In this case, one `Profile` can have
    # many `Article`s.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")

    cover = models.URLField(blank=True)
    description = models.TextField(blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name="articles", blank=True)

    objects = ArticleManager()

    class Meta:
        ordering = ["-created_at", "-updated_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "users:story", kwargs={"username": self.author.username, "slug": self.slug}
        )

    def save(self):
        ptitle = self.title.replace(" ", "-").lower()
        eslug = (self.title[:7] + str(self.created_at)).encode("utf-8").hex()[-12:]
        self.slug = slugify("%s-%s" % (ptitle, eslug))

        super(Article, self).save()
        return reverse("articles:articles")


class Comments(TimestampedModel):
    body = models.TextField()

    # Comments are related to article that commented at
    article = models.ForeignKey(
        Article, related_name="comments", on_delete=models.CASCADE
    )

    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
