from rest_framework import serializers
from User.models import Role, UserProfile


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    roleId = RoleSerializer(read_only=True, many=True)

    class Meta:
        model = UserProfile
        fields = "__all__"

