from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

# Create your views here.

def home(request):
    """Exemple page html"""
    text = """<h1>Hello World"""
    return HttpResponse(text)

def alexis(request):
	template = loader.get_template('index.html')
	return HttpResponse(template.render())