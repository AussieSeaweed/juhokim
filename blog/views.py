from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView, ListView

from blog.models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(draft=False)


class PostDetailView(PermissionRequiredMixin, DetailView):
    model = Post

    def has_permission(self):
        return not self.get_object().draft or self.request.user.is_staff


class PortfolioView(PostListView):
    template_name = 'blog/portfolio.html'

    def get_queryset(self):
        return super().get_queryset().filter(portfolio=True)
