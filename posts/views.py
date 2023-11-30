from rest_framework import generics, views, status, response, permissions
from .serializers import CommentSerializer
from .models import Comment, Post, Like
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]  # 인증된 사용자만 접근 가능


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 접근 가능

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return self.queryset.filter(post_id=self.kwargs['post_id'])


class LikeView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like, created = Like.objects.get_or_create(post=post, user=request.user)

        if not created:
            # 이미 좋아요가 존재하는 경우, 409 Conflict 반환
            return response.Response(status=status.HTTP_409_CONFLICT)

        return response.Response(status=status.HTTP_201_CREATED)

    def delete(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like = get_object_or_404(Like, post=post, user=request.user)
        like.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
    

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer