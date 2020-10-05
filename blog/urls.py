from django.urls import path

from .views import CategoryDetailView, PostDetailView, PortfolioView

urlpatterns = [
    path("categories/", CategoryDetailView.as_view(), name="blog-root"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("portfolio/", PortfolioView.as_view(), name="portfolio"),
]
