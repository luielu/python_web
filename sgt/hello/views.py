from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, World")
def Luiza(request):
    return HttpResponse("Hello, Luiza")
def Lerigou(request):
    return HttpResponse("Hello, Lerigou")
