from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from user.models import User
from user.serializers import UserSerializer


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
