from django.shortcuts import render
from django.http import HttpResponse
def index(request,id):
    return HttpResponse(f'''<h1> {id} </h1>''')

# Create your views here.
