from django.shortcuts import render
from django.http import HttpResponse
#from django.shortcuts import redirect

def home(request):
    return HttpResponse("<h1>Bem-vindo à minha página inicial do App Mercado!</h1>")

'''
def google_authenticate(request):
    return redirect('URL_DO_ENDPOINT_DO_GOOGLE')
'''