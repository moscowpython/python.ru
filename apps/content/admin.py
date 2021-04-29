from django.contrib import admin

from apps.content.models import Link, Slider


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'section', 'order', 'url']
    list_filter = ['section']
    list_editable = ['order']


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_visible', 'date', 'description']
