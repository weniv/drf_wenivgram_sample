from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    CommentCreateView,
    CommentListView,
    LikeView,
    PostDetailView,
)

urlpatterns = [
    path('posts/', PostCreateView.as_view(), name='post-create'),
    path('comments/', CommentCreateView.as_view(), name='comment-create'),
    path('posts/<int:post_id>/comments/', CommentListView.as_view(), name='comment-list'),
    path('posts/<int:post_id>/like/', LikeView.as_view(), name='post-like'),
    path('posts/list/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]