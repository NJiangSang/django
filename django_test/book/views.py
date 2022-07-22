from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    msg = "welcome to visit Dr.Cao's blog,2020!"
    return HttpResponse(msg)
