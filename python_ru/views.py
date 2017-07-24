from django.views.generic import View
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from cards.models import Card


class Api(View):

    def get(self, request):
        first_element = int(request.GET.get('from'))
        last_element = int(request.GET.get('to'))
        cards = Card.objects.all()[first_element:last_element]
        response_cards = []
        for card in cards:
            card_dict = {'url': card.url,
                         'image': card.image.path, #TODO fix image output
                         'type': card.type,
                         'preview': card.preview,
                         'category': card.category.title,
                         'title': card.title,
                         'has_button': card.has_button,
                         'button_text': card.button_text,
                         'button_url': card.button_url}
            response_cards.append(card_dict)
        return JsonResponse(response_cards, safe=False)
