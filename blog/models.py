from django.db.models import Model, ForeignKey, CharField, CASCADE, DateTimeField, BooleanField, ImageField
from ckeditor_uploader.fields import RichTextUploadingField


class Category(Model):
    parent = ForeignKey("Category", related_name="categories", on_delete=CASCADE, blank=True, null=True)
    name = CharField(max_length=255)
    description = CharField(max_length=255, blank=True)

    def __str__(self):
        if self.parent is None:
            return self.name + "/"
        else:
            return str(self.parent) + self.name + "/"

    class Meta:
        verbose_name_plural = "Categories"


class Post(Model):
    parent = ForeignKey(Category, related_name="posts", on_delete=CASCADE, blank=True, null=True)

    name = CharField(max_length=255)
    description = CharField(max_length=255, blank=True)
    draft = BooleanField(default=False)
    portfolio = BooleanField(default=False)

    created_on = DateTimeField(auto_now_add=True)
    updated_on = DateTimeField(auto_now=True)

    thumbnail = ImageField(upload_to="thumbnails", blank=True, null=True)
    content = RichTextUploadingField()

    def __str__(self):
        if self.parent is None:
            return self.name
        else:
            return str(self.parent) + self.name
