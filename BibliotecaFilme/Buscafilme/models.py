from django.db import models

class Ator(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    ano = models.IntegerField()
    diretor = models.CharField(max_length=100)
    atores = models.ManyToManyField(Ator)
    sinopse = models.TextField()

    def __str__(self):
        return self.titulo