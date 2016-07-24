from django.contrib import admin

from apps.content.models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'section', 'url']
    list_filter = ['section']
