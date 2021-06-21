from django import template

register = template.Library()


@register.filter
def get_token(string):
    return string.split('/')[-2:-1][0]
