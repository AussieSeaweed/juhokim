from django.urls import path

from blog.views import PortfolioView, PostDetailView, PostListView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
]
