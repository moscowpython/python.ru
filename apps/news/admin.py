from django.contrib import admin

from apps.news.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name', 'published_at', 'is_active', 'created']
