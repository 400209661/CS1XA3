from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('e/antemiaa/' , include('elmapp.urls')) ,
]
