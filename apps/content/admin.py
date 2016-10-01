from django.contrib import admin

from apps.content.models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'section', 'order', 'url']
    list_filter = ['section']
    list_editable = ['order']
