from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from apps.news import views as news_views


urlpatterns = [
    url(r'^$', news_views.IndexView.as_view(), name='index'),
    url(r'^meetups/', include('apps.meetups.urls')),
    url(r'^junior/$', news_views.JuniorView.as_view(), name='junior'),
    url(r'^post/(?P<pk>\d+)/$', news_views.PostView.as_view(), name='post_page'),

    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
