from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, trim_whitespace=True)
    group = serializers.CharField(write_only=True, trim_whitespace=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'group']

    def create(self, request):
        group_name = request.pop('group')
        user = User.objects.create_user(**request)
        group, _ = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)
        return user