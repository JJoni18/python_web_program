from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def john(request):
    return HttpResponse("Hello, John!")

def david(request):
    return HttpResponse("Hello, David")
