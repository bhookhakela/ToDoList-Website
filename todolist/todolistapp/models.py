from django.db import models

class TodoList(models.Model):
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
