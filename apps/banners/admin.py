from django.contrib import admin
from apps.banners.models import Banner, OutputTemplates, Position


class BannerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'date_from', 'date_to', 'date_days', 'priority', 'active')


class OutputTemplatesAdmin(admin.ModelAdmin):
    list_display = ('name', 'template')


class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'template')


admin.site.register(Banner, BannerAdmin)
admin.site.register(OutputTemplates, OutputTemplatesAdmin)
admin.site.register(Position, PositionAdmin)