from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    """Exemple page html"""
    text = """<h1>Hello World"""
    return HttpResponse(text)
