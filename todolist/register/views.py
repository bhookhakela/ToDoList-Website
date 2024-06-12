from django.shortcuts import render
# from django.contrib.auth import authenticate,login
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
def register(request):

    if request.method=="POST":
        registerform = RegistrationForm(request.POST)
        if registerform.is_valid():
            registerform.save()
            return HttpResponseRedirect("/login")
    else:
        registerform = RegistrationForm()
    return render(request, 'register/register.html',{'registerform':registerform})
# Create your views here.
