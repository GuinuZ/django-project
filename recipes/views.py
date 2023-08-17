from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(response):
    return render(response, 'recipes/home.html')


def contato(response):
    return HttpResponse("CONTATO")


def sobre(response):
    return HttpResponse("SOBRE")