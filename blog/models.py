from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import Model, ManyToManyField, CharField, DateTimeField, BooleanField, ImageField


class Tag(Model):
    name = CharField(max_length=255, unique=True)
    description = CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Post(Model):
    tags = ManyToManyField(Tag, related_name='posts', blank=True)

    title = CharField(max_length=255, unique=True)
    description = CharField(max_length=255, blank=True)

    draft = BooleanField(default=False)
    portfolio = BooleanField(default=False)

    created_on = DateTimeField(auto_now_add=True)
    updated_on = DateTimeField(auto_now=True)

    thumbnail = ImageField(upload_to='thumbnails', blank=True, null=True)
    content = RichTextUploadingField(blank=True)

    def __str__(self):
        return self.title
