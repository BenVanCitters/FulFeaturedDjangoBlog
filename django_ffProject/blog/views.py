from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Blog Home</ha>')

def about(request):
    return HttpResponse('<h1>Blog About</ha>')
