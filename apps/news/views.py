from django.views.generic import TemplateView

from apps.content.models import Link
from apps.events.models import Event
from apps.news.models import Article


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({
            'articles_top': Article.objects.active()[:3],
            'articles_all': Article.objects.active()[3:20],
            'events': Event.objects.active()[:5],
            'links': sorted(Link.objects.all(), key=lambda i: Link.SECTION_SLUGS.index(i.section)),
            'social_links': [
                {'id': 'fb', 'url': 'https://www.facebook.com/groups/MoscowDjango/', 'name': 'facebook'},
                {'id': 'twitter', 'url': 'https://twitter.com/moscowpython', 'name': 'twitter'}
            ]
        })
        return context
