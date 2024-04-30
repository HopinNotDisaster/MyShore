from django import template
from operate.models import UserCollects

register = template.Library()


@register.filter()
def has_collected(wallpaper, user):
    if UserCollects.objects.filter(wallpaper=wallpaper, user=user):
        return True
    return False
