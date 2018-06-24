from django.contrib import admin
from apps.banners.models import Banner, Position


class BannerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'date_from', 'date_to', 'date_days', 'priority', 'active')


class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'tag')


admin.site.register(Banner, BannerAdmin)
admin.site.register(Position, PositionAdmin)
