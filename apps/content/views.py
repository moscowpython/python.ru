import drawSvg as draw
from django.views.generic import TemplateView
from django.http import HttpResponse


def get_avatar(self, msg_text):

    d = draw.Drawing(90, 80, origin='center', displayInline=False)

    # Draw a circle
    d.append(draw.Circle(0, 0, 35, fill='#65AADD', stroke_width=2))

    if len(msg_text) < 5:
        font_size = 32
        cof = 7
    elif len(msg_text) < 7:
        font_size = 20
        cof = 7
    elif len(msg_text) <= 9:
        font_size = 15
        cof = 4
    else:
        font_size = 12
        cof = 3

    start_position = (len(msg_text) * cof) - (len(msg_text) * cof) - (len(msg_text) * cof)

    d.append(draw.Text(msg_text, font_size, start_position, -5, fill='#FFFFFF'))

    return HttpResponse(d.asSvg())
