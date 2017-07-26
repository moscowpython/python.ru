from django.core.management.base import BaseCommand, CommandError
from cards_api import factories


class Command(BaseCommand):
    help = 'Creates test data for development'

    categories_amount = 3
    cards_amount = 10

    def handle(self, *args, **options):
        for _ in range(self.categories_amount):
            factories.CardCategoryFactory.create()

        for _ in range(self.cards_amount):
            factories.CardFactory.create()
