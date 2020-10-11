from django.contrib.admin import register, ModelAdmin

from .models import Category, Post


@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ["name", "parent"]


@register(Post)
class PostAdmin(ModelAdmin):
    list_display = ["name", "parent", "draft", "portfolio", "created_on", "updated_on"]
