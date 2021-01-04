from django.conf import settings

from blog.views import PostListView


class HomeView(PostListView):
    template_name = 'juhokim/home.html'

    def get_queryset(self):
        return super().get_queryset()[:settings.RECENT_POST_COUNT]
