from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # 추가 필드 예시
    bio = models.TextField(blank=True) # 사용자 기분 정보
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
