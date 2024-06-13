from django.db import models
from django.contrib.auth.models import User
class TodoList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='todolist')
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Item(models.Model):
    name=models.CharField(max_length=100)
    todolist=models.ForeignKey(TodoList,on_delete=models.CASCADE)
    completed=models.BooleanField(default=False)
    def __str__(self):
        return self.name
# Create your models here.
