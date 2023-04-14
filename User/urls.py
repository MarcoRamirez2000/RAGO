from django.urls import path
from . import views
urlpatterns = [

    path('list/', views.UserFuncion, name = 'UserFuncion'),
    path('adduser/', views.AddUser, name = 'AddUser'),


]