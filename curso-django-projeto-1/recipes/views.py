from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse # dependencia da view - cria a response

def home(request): # view home
    return render(request,'recipes/home.html',status=201, context={'name':"Bruno"})