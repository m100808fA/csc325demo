from django.http import HttpResponse
from django.shortcuts import render

# Create tour views here

def home(request):
    return HttpResponse('<h1>Welcome to the home page</h1>')

def about(request):
    return HttpResponse('This is the about page.')