from django.utils.lorem_ipsum import *

from random import choice
from django.template.library import Library


register = Library()

@register.simple_tag
def custom_lorem_ipsum(count=155):
    c = 0
    words = []

    while c < count:
        word = choice(WORDS)
        words.append(word)
        c += 1

    return " ".join(words)[:count]
