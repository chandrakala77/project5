from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def first(request):
    return HttpResponse('first app1')

def first(request):
    return HttpResponse('second app1')