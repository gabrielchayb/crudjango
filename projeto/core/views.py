from django.shortcuts import render
from .models import Pessoa

# Create your views here.

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas': pessoas})

def salvar(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    idade = request.POST.get('idade')
    Pessoa.objects.create(nome=nome, email=email, idade=idade)
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {'pessoas': pessoas})  


