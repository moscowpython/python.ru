from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import ugettext as _

from apps.news.models import Article, HashTag


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
    list_display = ['admin_link', 'is_active', 'language', 'published_at', 'has_image', 'is_featured']
    list_filter = ['is_active', 'is_featured', HasImage, 'language', 'section']
    actions = ['make_active', 'make_inactive']
    list_display_links = None

    def admin_link(self, obj):
        url = reverse('admin:news_article_change', args=(obj.id,))
        return format_html('<a href={url}>{obj.name}</a>'
                           '<br><span style="color:#ccc">{obj.section}</span>'.format(url=url, obj=obj))

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


@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    list_display = ['name']
