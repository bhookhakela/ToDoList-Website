from django.contrib.auth import logout
from django.shortcuts import render
from .models import TodoList,Item
from django.http import HttpResponse, HttpResponseRedirect
from .forms import createlist
def index(request,id):
    t=TodoList.objects.get(id=id)
    if t.user==request.user:
        if request.method=='POST':
            print(request.POST)

            if request.POST.get('save'):

                for item in t.item_set.all():
                    if request.POST.get('c'+str(item.id))=='clicked':
                        item.completed=True
                    else:
                        item.completed=False
                    item.save()

            if request.POST.get('newitem'):
                text=request.POST.get('new')
                t.item_set.create(name=text)
        return render(request, "todolistapp/base.html", {"List": t})
    else:
        return HttpResponse('<h1>Access Denied! </h1><a href="/getlist/">View Your Lists</a>')



def home(request):
    if request.user.is_authenticated:
        return render(request, 'todolistapp/home.html')
    else:
        return HttpResponse("Please login first <a href='/login'>login</a>")

def newlist(request):

    if request.method=='POST':
        makeform = createlist(request.POST)
        if makeform.is_valid():
            name=makeform.cleaned_data['name']
            t=TodoList.objects.create(name=name,user=request.user)
            return HttpResponseRedirect(f"/{t.id}/")
    else:
        makeform = createlist()
    return render(request, 'todolistapp/newlist.html', {"form": makeform})
# Create your views here.
def user_logout(request):
    if request.method=='POST':
        logout(request)
        return HttpResponseRedirect("/")
    return render(request, 'todolistapp/logout.html')
def getlist(request):
    return render(request,"todolistapp/getlist.html")