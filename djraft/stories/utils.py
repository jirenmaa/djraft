
from django.utils import timezone
from django.utils.text import slugify
from unidecode import unidecode


def generate_slug(title: str, username: str):
    # decode all unknown string
    # then replace all `spaces` with `-`
    title = unidecode(title).replace(" ", "-").lower()

    # using `string encoded hex time` to improve slug
    # lol idk how to say it but yeah
    d = str(str(timezone.now()).encode("utf-8").hex()[30:42])
    n = str(username.encode("utf-8").hex()[:5])
    unique = d + n

    return slugify("%s-%s" % (title, unique))
