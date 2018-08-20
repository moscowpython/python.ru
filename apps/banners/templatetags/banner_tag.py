from django import template
from datetime import *
from functools import reduce
from apps.banners.models import Banner
from django.template import Context, Template, loader
from django.db.models import Q
from operator import or_

register = template.Library()


@register.simple_tag(takes_context=True)
def get_banner(context, place):
    """ banner """
    request = context.get('request')
    if not request:
        return ''

    now = datetime.now()
    nowtime = now.strftime("%H")

    weekday = ['128', '2', '4', '8', '16', '32', '64']
    day = []

    d = int(now.strftime('%w'))

    if d == 0:
        day.append(128)
        day.append(192)
        day.append(254)
    else:
        if d <= 5:
            day.append(weekday[d])
            day.append(62)
            day.append(254)
        else:
            day.append(weekday[d])
            day.append(192)
            day.append(254)

    all_banners = Banner.objects.filter(date_from__lte=now,
                                        date_to__gte=now,
                                        date_time_from__lte=nowtime,
                                        date_time_to__gte=nowtime,
                                        position__tag=place,
                                        active=True)
    banners = all_banners.filter(reduce(or_, [Q(date_days=dt) for dt in day]))

    if not banners:
        return ''

    banner = banners.first()

    response = loader.render_to_string("blocks/banner.html", {
        'image': banner.file_img,
        'place': place,
        'width': banner.width,
        'height': banner.height,
        'link_to': banner.link_to,
    })
    return response
