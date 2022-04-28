from unicodedata import name
from django import views
# from django.urls import render
# from django.http import JsonResponse
from django.urls import path
from.import views



urlpatterns = [
    path('', views.list, name='list'),
]

    
    
