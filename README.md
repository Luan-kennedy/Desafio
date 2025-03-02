# BibliotecaFilme
Aplicação Django para gerenciar diretores e filmes, com integração à API do OMDb para buscar informações sobre filmes.

# Funcionalidades
CRUD de Diretores:

Listar, visualizar detalhes, adicionar, editar e excluir diretores.

CRUD de Filmes:

Listar, visualizar detalhes, adicionar, editar e excluir filmes.

Busca de Filmes na API do OMDb:

Buscar informações sobre filmes (título, ano, diretor, gênero, sinopse, etc.) usando a API do OMDb.

Pré-requisitos
Python 3.8 ou superior.

Django 5.1 ou superior.

Biblioteca requests para consumir a API do OMDb.


# Como Usar
Página Inicial
Acesse http://127.0.0.1:8000/ para ver a página inicial.

A página inicial contém links para:

Listar diretores.

Adicionar um novo diretor.

Listar filmes.

Adicionar um novo filme.

Buscar filmes na API do OMDb.

## CRUD de Diretores
**Listar Diretores:** http://127.0.0.1:8000/diretores/

**Adicionar Diretor:** http://127.0.0.1:8000/diretor/novo/

**Editar Diretor:** http://127.0.0.1:8000/diretor/<id>/editar/

**Excluir Diretor:** http://127.0.0.1:8000/diretor/<id>/deletar/

## CRUD de Filmes
**Listar Filmes:** http://127.0.0.1:8000/filmes/

**Adicionar Filme:** http://127.0.0.1:8000/filme/novo/

**Editar Filme:** http://127.0.0.1:8000/filme/<id>/editar/

**Excluir Filme:** http://127.0.0.1:8000/filme/<id>/deletar/

##**Buscar Filme na API do OMDb**
Acesse http://127.0.0.1:8000/buscar-filme/.

Digite o título de um filme e clique em "Buscar".

As informações do filme serão exibidas, incluindo título, ano, diretor, gênero, sinopse e poster.
