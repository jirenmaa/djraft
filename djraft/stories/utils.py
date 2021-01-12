
from django.utils import timezone as djtimezone
from django.utils.text import slugify
from unidecode import unidecode
from datetime import datetime, timedelta, timezone


def generate_slug(title: str, username: str):
    # decode all unknown string
    # then replace all `spaces` with `-`
    title = unidecode(title).replace(" ", "-").lower()

    # using `string encoded hex time` to improve slug
    # lol idk how to say it but yeah
    d = str(str(djtimezone.now()).encode("utf-8").hex()[30:42])
    n = str(username.encode("utf-8").hex()[:5])
    unique = d + n

    return slugify("%s-%s" % (title, unique))


def convert_timedelta(duration):
    days, seconds = abs(duration.days), duration.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    # return hours, minutes, seconds
    return '{} hours, {} minutes, {} seconds'.format(hours, minutes, seconds)
