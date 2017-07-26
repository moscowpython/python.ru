from django.views.generic import View
from django.http import JsonResponse

from cards_api.models import Card


class CardsListJsonView(View):
    DEFAULT_CARDS_AMOUNT = '100'

    def get(self, request):
        first_element = int(request.GET.get('from', '0'))
        last_element = int(request.GET.get('to', self.DEFAULT_CARDS_AMOUNT))
        cards = self.fetch_cards(first_element, last_element)
        return JsonResponse({
            'data': [c.to_dict() for c in cards],
            'meta': {
                'from': first_element,
                'to': last_element
            },
        })

    def fetch_cards(self, first_element, last_element):
        return Card.objects.all()[first_element:last_element]
