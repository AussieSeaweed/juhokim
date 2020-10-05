from django.contrib import admin
from django.forms import ModelForm, CharField
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Category, Post

admin.site.register(Category)


class PostAdminForm(ModelForm):
    content = CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
