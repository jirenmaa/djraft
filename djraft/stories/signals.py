from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Story, Like, Dislike


@receiver(post_save, sender=Story)
def create_story(sender, instance, created, **kwargs):
    if created:
        Like.objects.create(story=instance)
        Dislike.objects.create(story=instance)
