from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('filme/<int:filme_id>/', views.filme_detail, name='filme_detail'),
]