from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
def register(request):

    if request.method=="POST":
        loginform = UserCreationForm(request.POST)
        if loginform.is_valid():
            loginform.save()
        # print(request.POST)
    else:
        loginform = UserCreationForm()
    return render(request, 'register/register.html',{'loginform':loginform})
# Create your views here.
