from django.urls import path

from .views import PostDetailView, PortfolioView

urlpatterns = [
    path('posts/', PortfolioView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
]
