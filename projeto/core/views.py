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

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, 'update.html', {'pessoa': pessoa})

def update(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = request.POST.get('nome')
    pessoa.email = request.POST.get('email')
    pessoa.idade = request.POST.get('idade')
    pessoa.save()
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas': pessoas})
