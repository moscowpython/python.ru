from django.contrib import admin
from django.utils.translation import ugettext as _

from apps.news.models import Article


class HasImage(admin.SimpleListFilter):
    title = _('Есть картинка')
    parameter_name = 'image'

    def lookups(self, request, model_admin):
        return (
            ('yes', _('Есть')),
            ('not', _('Нет')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.exclude(image='')
        if self.value() == 'no':
            return queryset.filter(image='')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name', 'published_at', 'is_active', 'created', 'has_image', 'is_featured']
    list_filter = ['is_active', 'is_featured', HasImage]
    actions = ['make_active', 'make_inactive']

    def has_image(self, obj):
        return bool(obj.image)
    has_image.short_description = 'Картинка'
    has_image.boolean = True

    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    make_active.short_description = 'Опубликовать'

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_inactive.short_description = 'Снять с публикации'
