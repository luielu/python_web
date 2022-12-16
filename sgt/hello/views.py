from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return render(request, "hello/index.html")
    
def Luiza(request):
    return HttpResponse("Hello, Luiza")
def Lerigou(request):
    return HttpResponse("Hello, Lerigou")
    
def greet(request, name):
    return render(request, "hello/greet.html",{
    	"name":name.capitalize()
    	})
