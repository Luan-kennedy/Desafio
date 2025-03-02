from django.shortcuts import render, redirect, get_object_or_404
import requests
from .models import Filme, Ator
from .forms import BuscarFilmeForm 

def home(request):
    if request.method == 'POST':
        form = BuscarFilmeForm(request.POST) 
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            api_key = "82868d81"  # chave da API OMDb
            url = f'http://www.omdbapi.com/?i=tt3896198&apikey=82868d81'
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