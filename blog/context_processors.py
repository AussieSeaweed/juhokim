from django.conf import settings

from .models import Post


def blog(request):
    return {
        "recent_posts": Post.objects.filter(draft=False).order_by("created_on")[:settings.NUM_RECENT_POSTS],
    }
