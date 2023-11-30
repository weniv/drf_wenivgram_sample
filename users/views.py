from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions

User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # 모든 사용자 접근 가능
    # settings.py의 REST_FRAMEWORK에 설정된 기본 permission_classes를 덮어쓰기 위해 설정
    permission_classes = [permissions.AllowAny]

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer