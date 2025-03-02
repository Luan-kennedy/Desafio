from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('filme/<int:filme_id>/', views.filme_detail, name='filme_detail'),

    # CRUD para Filme
    path('filme/novo/', views.filme_create, name='filme_create'),
    path('filme/editar/<int:filme_id>/', views.filme_update, name='filme_update'),
    path('filme/excluir/<int:filme_id>/', views.filme_delete, name='filme_delete'),

     # CRUD para Ator
    path('ator/novo/', views.ator_create, name='ator_create'),
    path('ator/editar/<int:ator_id>/', views.ator_update, name='ator_update'),
    path('ator/excluir/<int:ator_id>/', views.ator_delete, name='ator_delete')
]