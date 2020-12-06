from django.conf import settings

from .models import Post


def blog(request):
    return {
        'recent_posts': Post.objects.filter(draft=False)[:settings.NUM_RECENT_POSTS],
    }
