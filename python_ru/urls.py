from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from apps.news import views as news_views
from apps.content import views as content_views


urlpatterns = [
    url(r'^$', news_views.IndexView.as_view(), name='index'),
    url(r'^blog/$', news_views.BlogView.as_view(), name='blog'),
    url(r'^events/$', news_views.EventsView.as_view(), name='events'),
    url(r'^tag/(?P<name_tag>\w+)$', news_views.TagView.as_view(), name='tag'),
    url(r'^get-avatar/(?P<msg_text>\w+).svg$', content_views.get_avatar, name='get_avatar'),
    url(r'^meetups/', include('apps.meetups.urls')),
    url(r'^junior/$', news_views.JuniorView.as_view(), name='junior'),
    url(r'^post/(?P<pk>\d+)/$', news_views.PostView.as_view(), name='post_page'),

    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()