from django.views.generic import RedirectView
from django.views.generic import TemplateView

from apps.content.models import Link
from apps.events.models import Event
from apps.news.models import Article


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        article_featured = Article.objects.featured()
        context.update({
            'article_featured': article_featured,
            'articles_top': [a for a in Article.objects.active()[:3] if a != article_featured],
            'articles_all': [a for a in Article.objects.active()[3:10] if a != article_featured],
            'events': Event.objects.upcoming()[:5],
            'links': sorted(Link.objects.all(), key=lambda i: Link.SECTION_SLUGS.index(i.section)),
            'social_links': [
                {'id': 'facebook', 'url': 'https://www.facebook.com/groups/MoscowDjango/', 'name': 'facebook'},
                {'id': 'twitter', 'url': 'https://twitter.com/moscowpython', 'name': 'twitter'},
                {'id': 'slack', 'url': 'https://python.stamplayapp.com/', 'name': 'slack'},
            ]
        })
        return context


class JuniorView(RedirectView):
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        return '/meetups/junior/'  # FIXME: make this alive
