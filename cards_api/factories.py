import factory
from factory.fuzzy import FuzzyChoice

from cards_api.models import Card, CardCategory


class CardCategoryFactory(factory.DjangoModelFactory):
    title = factory.Faker('word')
    slug = factory.LazyAttribute(lambda obj: obj.title.lower())

    class Meta:
        model = 'cards_api.CardCategory'


class CardFactory(factory.DjangoModelFactory):
    type = FuzzyChoice(Card.STATUS._db_values)
    url = factory.Faker('uri')
    image = factory.django.ImageField(width=300, height=180)
    category = factory.Iterator(CardCategory.objects.all())
    title = factory.Faker('text', max_nb_chars=100)
    preview = factory.Faker('text', max_nb_chars=300)
    has_button = FuzzyChoice([True, False])
    button_text = factory.Faker('word')
    button_url = factory.Faker('uri')

    class Meta:
        model = 'cards_api.Card'
