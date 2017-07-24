from django.conf.urls import url
from python_ru.views import Api
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', Api.as_view()),
]
