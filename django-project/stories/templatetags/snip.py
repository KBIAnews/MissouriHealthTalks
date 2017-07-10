from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='snip')
@stringfilter
def snip(value):
    return value.splitlines()[0]
