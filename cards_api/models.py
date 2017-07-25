from django.db import models
from model_utils.models import TimeStampedModel, StatusModel
from model_utils.fields import StatusField
from model_utils import Choices


class CardCategory(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField()


class Card(TimeStampedModel, StatusModel):
    STATUS = Choices(
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    TYPE_CHOICES = Choices(
        ('url', 'Url'),
        ('event', 'Event'),
        ('banner', 'Banner'),
    )

    type = StatusField(choices_name='TYPE_CHOICES')

    url = models.URLField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey('CardCategory', null=True, blank=True)
    title = models.CharField(max_length=512)
    preview = models.CharField(max_length=1024)

    has_button = models.BooleanField(default=False)
    button_text = models.CharField(max_length=20, null=True, blank=True)
    button_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'url': self.url,
            'image': self.image.url if self.image else None,
            'type': self.type,
            'preview': self.preview,
            'category_id': self.category_id,
            'category_name': self.category.title if self.category else None,
            'title': self.title,
            'has_button': self.has_button,
            'button_text': self.button_text,
            'button_url': self.button_url,
        }
