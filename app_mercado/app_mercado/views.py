from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bem-vindo à minha página inicial do App Mercado!</h1>")