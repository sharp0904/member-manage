from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader

def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

# Create your views here.
