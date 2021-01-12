from django.utils.lorem_ipsum import *

from django.template.library import Library


register = Library()

@register.simple_tag
def last_update(create_date):
    pass
