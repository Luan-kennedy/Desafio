from django.urls import path
from . import views

urlpatterns = [
    path('diretores/', views.lista_diretores, name='lista_diretores'),
    path('diretor/<int:pk>/', views.detalhes_diretor, name='detalhes_diretor'),
    path('diretor/novo/', views.novo_diretor, name='novo_diretor'),
    path('diretor/<int:pk>/editar/', views.editar_diretor, name='editar_diretor'),
    path('diretor/<int:pk>/deletar/', views.deletar_diretor, name='deletar_diretor'),
    path('filmes/', views.lista_filmes, name='lista_filmes'),
    path('filme/<int:pk>/', views.detalhes_filme, name='detalhes_filme'),
    path('filme/novo/', views.novo_filme, name='novo_filme'),
    path('filme/<int:pk>/editar/', views.editar_filme, name='editar_filme'),
    path('filme/<int:pk>/deletar/', views.deletar_filme, name='deletar_filme'),
    path('buscar-filme/', views.buscar_filme, name='buscar_filme'),
]