from django import template

from apps.content.models import Link

register = template.Library()


@register.filter
def get_section_name(section_slug):
    return Link(section=section_slug).get_section_display()
