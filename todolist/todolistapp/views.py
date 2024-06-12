from django.contrib.auth import logout
from django.shortcuts import render
from .models import TodoList,Item
from django.http import HttpResponse, HttpResponseRedirect
from .forms import createlist
def index(request,id):
    t=TodoList.objects.get(id=id)

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
def home(request):
    print(request.user.is_authenticated)
    return render(request, 'todolistapp/home.html')

def newlist(request):

    if request.method=='POST':
        makeform = createlist(request.POST)
        if makeform.is_valid():
            name=makeform.cleaned_data['name']
            t=TodoList.objects.create(name=name)
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