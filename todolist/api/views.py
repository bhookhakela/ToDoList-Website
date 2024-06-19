from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from todolistapp.models import TodoList
from . import serializers
class alllists(generics.ListAPIView):
    model=TodoList
    # queryset = TodoList.objects.all().filter(user=self.request.user)
    permission_classes = [permissions.IsAuthenticated]
    serializer_class=serializers.TodoListSerializer
    def get_queryset(self):
        return TodoList.objects.filter(user=self.request.user)
    # def get(self, request, *args, **kwargs):
    #     if queryset.user==request.user:

class Login(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        username=request.data['username']
        password=request.data['password']
        result=authenticate(request, username=username, password=password)
        if result:
            login(request, result)
            return Response("Login Successful", status=status.HTTP_200_OK)
        else:
            return Response("Invalid Credentials", status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
