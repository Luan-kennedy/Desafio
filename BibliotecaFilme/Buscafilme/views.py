from django.shortcuts import render, redirect, get_object_or_404
import requests
from .models import Filme, Ator
from .forms import BuscarFilmeForm
from django.forms import modelform_factory

def home(request):
    if request.method == 'POST':
        form = BuscarFilmeForm(request.POST) 
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            api_key = "82868d81"  # chave da API OMDb
            url = f'http://www.omdbapi.com/?i=tt3896198&apikey=82868d81&'
            response = requests.get(url)
            data = response.json()

            if data.get('Response') == 'True':
                filme, created = Filme.objects.get_or_create(
                    titulo=data['Title'],
                    defaults={
                        'ano': int(data['Year']),
                        'diretor': data['Director'],
                        'sinopse': data['Plot']
                    }
                )
                atores = data['Actors'].split(', ')
                for nome in atores:
                    ator, created = Ator.objects.get_or_create(nome=nome.strip())
                    filme.atores.add(ator)
                return redirect('filme_detail', filme_id=filme.id)
            else:
                return render(request, 'Buscafilme/home.html', {
                    'form': form,
                    'error': 'Filme não encontrado'
                })
    else:
        form = BuscarFilmeForm()

    return render(request, 'Buscafilme/home.html', {'form': form})

def filme_detail(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    return render(request, 'Buscafilme/filme_detail.html', {'filme': filme})


# CRUD para Filme
def filme_create(request):
    if request.method == 'POST':
        form = modelform_factory(Filme, fields=('titulo', 'ano', 'diretor', 'sinopse', 'atores'))(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = modelform_factory(Filme, fields=('titulo', 'ano', 'diretor', 'sinopse', 'atores'))()
    return render(request, 'Buscafilme/filme_form.html', {'form': form})


def filme_update(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    if request.method == 'POST':
        form = modelform_factory(Filme, fields=('titulo', 'ano', 'diretor', 'sinopse', 'atores'))(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('filme_detail', filme_id=filme.id)
    else:
        form = modelform_factory(Filme, fields=('titulo', 'ano', 'diretor', 'sinopse', 'atores'))(instance=filme)
    return render(request, 'Buscafilme/filme_form.html', {'form': form})


def filme_delete(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    if request.method == 'POST':
        filme.delete()
        return redirect('home')
    return render(request, 'Buscafilme/filme_confirm_delete.html', {'filme': filme})

# CRUD para Ator
def ator_create(request):
    if request.method == 'POST':
        form = modelform_factory(Ator, fields=('nome', 'data_nascimento'))(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = modelform_factory(Ator, fields=('nome', 'data_nascimento'))()
    return render(request, 'Buscafilme/ator_form.html', {'form': form})


def ator_update(request, ator_id):
    ator = get_object_or_404(Ator, id=ator_id)
    if request.method == 'POST':
        form = modelform_factory(Ator, fields=('nome', 'data_nascimento'))(request.POST, instance=ator)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = modelform_factory(Ator, fields=('nome', 'data_nascimento'))(instance=ator)
    return render(request, 'Buscafilme/ator_form.html', {'form': form})


def ator_delete(request, ator_id):
    ator = get_object_or_404(Ator, id=ator_id)
    if request.method == 'POST':
        ator.delete()
        return redirect('home')
    return render(request, 'Buscafilme/ator_confirm_delete.html', {'ator': ator})