from django.db.migrations import serializer
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# from rest_framework.parsers import JSONParser
from rest_framework_simplejwt.authentication import JWTAuthentication

import User
from User.models import Role, UserProfile
from User.serializers import RoleSerializer, UserProfileSerializer


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def RoleApi(request, role_ID=None):
    if request.method == 'GET':
        _id = role_ID
        if _id is not None:
            role = Role.objects.get(role_ID=_id)
            roleSerializer = RoleSerializer(role)
            return Response(roleSerializer.data, status.HTTP_200_OK)

        role = Role.objects.all()
        roleSerializer = RoleSerializer(role, many=True)
        return Response(roleSerializer.data, status.HTTP_200_OK)

    if request.method == 'POST':
        role_serializer = RoleSerializer(data=request.data)
        if role_serializer.is_valid():
            role_serializer.save()
            return Response("Role Added!!!", status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = role_ID
        role = Role.objects.get(role_ID=id)
        role_serializer = RoleSerializer(role, data=request.data)
        if role_serializer.is_valid():
            role_serializer.save()
            return Response({'MSG': 'Data Updated'}, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        id = role_ID
        role = Role.objects.get(role_ID=id)
        role_serializer = RoleSerializer(role, data=request.data, partial=True)
        if role_serializer.is_valid():
            role_serializer.save()
            return Response({'MSG': ' Partial Data Updated'}, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        id = role_ID
        role = Role.objects.get(role_ID=id)
        role.delete()
        return Response({'MSG': 'Role Deleted'}, status.HTTP_200_OK)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def UserProfileApi(request, user_id=None):
    if request.method == 'GET':
        _id = user_id
        if _id is not None:
            user = UserProfile.objects.get(user_id=_id)
            userSerializer = UserProfileSerializer(user)
            return Response(userSerializer.data, status.HTTP_200_OK)

        user = UserProfile.objects.all()
        userSerializer = UserProfileSerializer(user, many=True)
        return Response(userSerializer.data, status.HTTP_200_OK)

    if request.method == 'POST':
        user_serializer = UserProfileSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response("Role Added!!!", status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = user_id
        user = UserProfile.objects.get(user_id=id)
        user_serializer = UserProfileSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'MSG': 'Data Updated'}, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        id = user_id
        user = UserProfile.objects.get(user_id=id)
        user_serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'MSG': ' Partial Data Updated'}, status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        id = user_id
        role = Role.objects.get(user_id=id)
        role.delete()
        return Response({'MSG': 'Role Deleted'}, status.HTTP_200_OK)
