from django import template

register = template.Library()

from libgravatar import Gravatar

@register.filter
def gravatar(user):
    email = user.email.lower().encode('utf-8')
    g = Gravatar(email)
    url = g.get_profile()
    return url