# coding: utf-8
import factory

from apps.content.models import Link


class LinkFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: u"link%s" % n)
    url = factory.Sequence(lambda n: u"http://moscowpython.ru/meetups/%s" % n)
    section = 'courses'
    order = factory.Sequence(lambda n: n)

    class Meta:
        model = Link
