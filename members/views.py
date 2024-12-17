from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def members(request):
    return HttpResponse("Hello world!")

# Create your views here.
