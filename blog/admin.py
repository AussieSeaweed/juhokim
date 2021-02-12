from django.contrib.admin import ModelAdmin, register

from blog.models import Post, Tag


@register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ['name']


@register(Post)
class PostAdmin(ModelAdmin):
    list_display = ['title', 'draft', 'portfolio', 'created_on', 'updated_on']
