from django.utils.lorem_ipsum import *

from random import choice
from django.template.defaultfilters import linebreaksbr, slice_filter
from django.template.library import Library


register = Library()

@register.simple_tag
def context_length(value, _slice):
    if len(value) > _slice:
        value = slice_filter(value, _slice) + " ..."
        return value

    return value
