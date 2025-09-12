from django.shortcuts import render
from .models import Pessoa

# Create your views here.
def home(request):
    return render(request,'index.html')

def arquivo(request):
    nome = 'Pedro'
    idade = "17"

    return render(request, 'arquivo.html',{'nome': nome, "idade": idade})


def lista_pessoas(request):
    pessoas = Pessoa.objects.all().order_by('nome')
    return render(request, 'pessoas.html', {'pessoas': pessoas})

def criados(request):
    return render(request,'criados.html')

def criar_post(request):
    return render(request,'criar_post.html')

def carrossel(request):
    return render(request,'carrossel.html')

def recomendados(request):
    return render(request,'recomendados.html')

def sobre(request):
    return render(request,'sobre.html')

def login(request):
    return render(request,'login.html')

def registrar(request):
    return render(request,'registar.html')