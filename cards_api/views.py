from django.views.generic import View
from django.http import JsonResponse
from cards_api.models import Card


class CardsListJsonView(View):

    def get(self, request):
        default_first_elem = 0
        default_last_elem = len(Card.objects.all())
        first_element = int(request.GET.get('from', default_first_elem))
        last_element = int(request.GET.get('to', default_last_elem))
        cards = Card.objects.all()[first_element:last_element]
        response_cards = []
        for card in cards:
            card_dict = {'url': card.url,
                         'image': card.image.url,
                         'type': card.type,
                         'preview': card.preview,
                         'category': card.category.title,
                         'title': card.title,
                         'has_button': card.has_button,
                         'button_text': card.button_text,
                         'button_url': card.button_url}
            meta = {'from': first_element,
                    'to': last_element}
            image_info_dict = {'data': response_cards,
                               'meta': meta}
            response_cards.append(card_dict)
        meta = {'from': first_element,
                'to': last_element}
        image_info_dict = {'data': response_cards,
                           'meta': meta}
        return JsonResponse(image_info_dict)
