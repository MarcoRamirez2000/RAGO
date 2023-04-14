from django.shortcuts import render, redirect
from django.apps import apps
# import pyodbc

from .models import *

# Create your views here.


# def index(request):
#     Fonos = []
#     return render(request, 'index.html', {'Fonos':Fonos})

def home(request):
    print()
    return render(request, 'index.html')