# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt

'''
<div id="top-banner" class="conf">
    <a href="http://conf.python.ru/?utm_source=python-ru&amp;utm_medium=banner&amp;utm_campaign=python-ru-top" target="_blank"></a>
</div>
'''


def get_banner():
    pass  # ToDo:


@csrf_exempt
def clicke_banner(request):
    pass  # ToDo:
