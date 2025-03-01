from django.shortcuts import render, get_object_or_404, redirect
from .models import Diretor, Filme
from .forms import DiretorForm, FilmeForm
import requests

def lista_diretores(request):
    diretores = Diretor.objects.all()
    return render(request, 'Buscafilme/lista_diretores.html', {'diretores':diretores})

def detalhes_diretor(request, pk):
    diretor = get_object_or_404(Diretor, pk=pk)
    return render(request,'Buscafilme/detalhes_diretor.html', {'diretor': diretor})

def novo_diretor(request):
    if request.method == "POST":
        form = DiretorForm(request.POST)
        if form.is_valid():
            diretor = form.save()
            return redirect('detalhes_diretor', pk=diretor.pk)
    else:
        form = DiretorForm()
    return render(request, 'Buscafilme/editar_diretor.html', {'form': form})

def editar_diretor(request, pk):
    diretor = get_object_or_404(Diretor, pk=pk)
    if request.method == "POST":
        form = DiretorForm(request.POST, instance=diretor)
        if form.is_valid():
            diretor = form.save()
            return redirect('detalhes_diretor', pk=diretor.pk)
    else:
        form = DiretorForm(instance=diretor)
    return render(request, 'Buscafilme/editar_diretor.html', {'form': form})

def deletar_diretor(request, pk):
    diretor = get_object_or_404(Diretor, pk=pk)
    diretor.delete()
    return redirect('lista_diretores')

# Views para Filme mesma logica para Diretor

def lista_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'Buscafilme/lista_filmes.html', {'filmes': filmes})

def detalhes_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    return render(request, 'Buscafilme/detalhes_filme.html', {'filme': filme})

def novo_filme(request):
    if request.method == "POST":
        form = FilmeForm(request.POST)
        if form.is_valid():
            filme = form.save()
            return redirect('detalhes_filme', pk=filme.pk)
    else:
        form = FilmeForm()
    return render(request, 'Buscafilme/editar_filme.html', {'form': form})

def editar_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    if request.method == "POST":
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            filme = form.save()
            return redirect('detalhes_filme', pk=filme.pk)
    else:
        form = FilmeForm(instance=filme)
    return render(request, 'Buscafilme/editar_filme.html', {'form': form})

def deletar_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    filme.delete()
    return redirect('lista_filmes')

# View para buscar filmes na API do OMDb
def buscar_filme(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        api_key = "82868d81"  # chave da API OMDb
        url = f" http://www.omdbapi.com/?i=tt3896198&apikey=82868d81"
        response = requests.get(url)
        filme_info = response.json()
        return render(request, 'Buscafilme/buscar_filme.html', {'filme_info': filme_info})
    return render(request, 'Buscafilme/buscar_filme.html')