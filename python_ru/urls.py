from django.conf.urls import url
from python_ru.views import CardsListJsonView
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', CardsListJsonView.as_view()),
]
