from django.shortcuts import render, redirect
from django.apps import apps
# import pyodbc
from .forms import *
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .models import *



from django.contrib.auth.decorators import login_required

@login_required
def UserFuncion(request):

    return render(request, 'Users.html', {})



@login_required
def  AddUser(request):
    form=[]
    return render(request, 'AddUser.html', {'form': form})



        