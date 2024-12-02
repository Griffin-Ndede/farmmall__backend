from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

class Home(View):
    def get(self, request):
        return HttpResponse("Hello world!")

class Register(View):
    def get(self, request):
        return HttpResponse("I have registered to use this platform finally")
    
class Login(View):
    def get(self, request):
        return HttpResponse("I have logged in to the platform and I can now use it")
    
class Crops(View):
    def get(self, request):
        return HttpResponse("These are the crops that have been listed on the platform")


