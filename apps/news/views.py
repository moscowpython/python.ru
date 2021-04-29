from django.views.generic import RedirectView
from django.views.generic import TemplateView

from apps.content.models import Link, Slider
from apps.events.models import Event
from apps.news.models import Article, HashTag


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        article_featured = Article.objects.filter(is_active=True).order_by("-published_at")[:10]
        context.update({
            'articles': article_featured,
            'slider': Slider.objects.filter(is_visible=True),
            'events': Event.objects.upcoming()[:2],
            'links': sorted(Link.objects.all(), key=lambda i: Link.SECTION_SLUGS.index(i.section)),
            'tags': HashTag.objects.all(),
            "page": "index",
            'social_links': [
                {'id': 'facebook', 'url': 'https://www.facebook.com/groups/MoscowDjango/', 'name': 'facebook'},
                {'id': 'twitter', 'url': 'https://twitter.com/moscowpython', 'name': 'twitter'},
                {'id': 'slack', 'url': 'http://slack.python.ru/', 'name': 'slack'},
            ]
        })
        return context


class PostView(TemplateView):
    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        pk = self.kwargs.get('pk')
        post = Article.objects.get(id=pk)

        article_featured = Article.objects.featured()
        context.update({
            'article_featured': article_featured,
            'articles_top': [a for a in Article.objects.active()[:4] if a != article_featured],
            'events': Event.objects.upcoming()[:2],
            'post': post,
            "page": "post",
            'links': sorted(Link.objects.all(), key=lambda i: Link.SECTION_SLUGS.index(i.section)),
            'social_links': [
                {'id': 'facebook', 'url': 'https://www.facebook.com/groups/MoscowDjango/', 'name': 'facebook'},
                {'id': 'twitter', 'url': 'https://twitter.com/moscowpython', 'name': 'twitter'},
                {'id': 'slack', 'url': 'http://slack.python.ru/', 'name': 'slack'},
            ],
            "similar_posts": Article.objects.filter(is_recommend=True)[:5]
        })
        return context


class BlogView(TemplateView):
    template_name = "blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        article = Article.objects.filter(is_active=True).order_by("-published_at")[:10]
        context.update({
            'posts': article,
            'events': Event.objects.upcoming()[:2],
            'links': sorted(Link.objects.all(), key=lambda i: Link.SECTION_SLUGS.index(i.section)),
            'tags': HashTag.objects.all(),
            "page": "blog",
            'social_links': [
                {'id': 'facebook', 'url': 'https://www.facebook.com/groups/MoscowDjango/', 'name': 'facebook'},
                {'id': 'twitter', 'url': 'https://twitter.com/moscowpython', 'name': 'twitter'},
                {'id': 'slack', 'url': 'http://slack.python.ru/', 'name': 'slack'},
            ]
        })
        return context


class JuniorView(RedirectView):
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        return '/meetups/junior/'  # FIXME: make this alive


class EventsView(TemplateView):
    template_name = "events.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({
            "page": "events",
        })
        return context
