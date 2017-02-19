from django.views.generic import DetailView

from apps.events.models import Event


class EventDetailView(DetailView):
    model = Event
    slug_url_kwarg = 'event_slug'
    template_name = 'meetups/event_detail.html'
