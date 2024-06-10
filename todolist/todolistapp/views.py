from django.shortcuts import render
from .models import TodoList,Item
from django.http import HttpResponse
from .forms import createlist
def index(request,id):
    t=TodoList.objects.get(id=id)
    return render(request, "todolistapp/base.html", {"List": t})
def home(request):
    return render(request, 'todolistapp/home.html')

def newlist(request):
    makeform=createlist()
    return render(request, 'todolistapp/newlist.html', {"form": makeform})
# Create your views here.
