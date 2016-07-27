from django.contrib import admin

from apps.events.models import Event, City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    ...


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'date', 'is_active', 'url']
    list_filter = ['city']
