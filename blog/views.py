from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView, ListView

from .models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(PermissionRequiredMixin, DetailView):
    model = Post

    def has_permission(self):
        return not self.get_object().draft or self.request.user.is_staff


class PortfolioView(PostListView):
    template_name = 'blog/portfolio.html'

    def get_queryset(self):
        return Post.objects.filter(draft=False, portfolio=True)
