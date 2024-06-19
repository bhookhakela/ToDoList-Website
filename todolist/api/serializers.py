from rest_framework import serializers
from todolistapp import models
class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.TodoList
        fields=['name']