from django.utils.text import slugify

from random import randint

def generate_slug(title, created_at):
    title = title.replace(" ", "-").lower()
    unique = (title[:7] + str(created_at)).encode("utf-8").hex()[-12:]
    slug = slugify("%s-%s" % (title, unique))

    return slug

