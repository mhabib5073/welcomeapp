from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    s="<h1>hellow welcome to django</h1>"
    return HttpResponse(s)
