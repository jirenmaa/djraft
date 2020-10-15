from django import template

register = template.Library()


@register.filter(name='addclass')
def addclass(value, args):
    return value.as_widget(attrs={'class': args})


@register.filter(name='wtype')
def wtype(args):
    return type(args)
