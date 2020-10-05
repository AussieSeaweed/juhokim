from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Category, Post


class CategoryDetailView(DetailView):
    model = Category

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except AttributeError:
            return None

    def get_context_data(self, **kwargs):
        category = self.get_object()

        return {
            **super().get_context_data(**kwargs),
            "categories": Category.objects.filter(
                parent__isnull=True) if category is None else category.categories.all(),
            "posts": Post.objects.filter(parent__isnull=True,
                                         draft=False) if category is None else category.posts.filter(draft=False),
        }


class PostDetailView(DetailView, PermissionRequiredMixin):
    model = Post

    def has_permission(self):
        return self.get_object().draft or self.request.user.is_authenticated


class PortfolioView(ListView):
    template_name = "blog/portfolio.html"

    def get_queryset(self):
        return Post.objects.filter(draft=False, portfolio=True)
