from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(?P<event_slug>\w+)/$', views.EventDetailView.as_view(), name='event_detail_view'),
]
