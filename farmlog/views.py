from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello world!")

def register(request):
    return HttpResponse("I have registered to use the platform")

def login(request):
    return HttpResponse("I have logged in to the platform")

def crops(request):
    return HttpResponse("These are the crops that have been listed on the platform")

