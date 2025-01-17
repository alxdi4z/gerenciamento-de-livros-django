from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny

from api.serializers.UserSerializer import UserCreateSerializer

User = get_user_model()
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]