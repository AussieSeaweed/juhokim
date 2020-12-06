from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, blank=True)

    draft = models.BooleanField(default=False)
    portfolio = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    content = RichTextUploadingField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_on']
