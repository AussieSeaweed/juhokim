from django.contrib.admin import register, ModelAdmin

from .models import Tag, Post


@register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ['name']


@register(Post)
class PostAdmin(ModelAdmin):
    list_display = ['title', 'draft', 'portfolio', 'created_on', 'updated_on']
