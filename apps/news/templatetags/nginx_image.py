# coding: utf-8
# https://github.com/adw0rd/django-nginx-image/blob/master/nginx_image/templatetags/nginx_image.py
from django import template
from django.conf import settings
from django.db.models.fields.files import FieldFile

register = template.Library()


@register.simple_tag
def thumbnail(image_url, width="-", height="-", crop=False):
    if getattr(settings, 'DISABLE_RESIZER', False):
        url = image_url
        if isinstance(image_url, FieldFile):
            if getattr(image_url, 'name', None) and hasattr(image_url, 'url'):
                url = image_url.url
        return url
    method = "crop" if crop else "resize"
    if not settings.DEBUG:
        url = "/{method}/{w}/{h}".format(
            method=method,
            w=width if width else "-",
            h=height if height else "-")
    else:
        url = ""
    if isinstance(image_url, FieldFile):
        if getattr(image_url, 'name', None) and hasattr(image_url, 'url'):
            url += image_url.url
    else:
        url += image_url
    return url
