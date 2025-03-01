from django.db import models

class Diretor(models.Model):
    nome = models.CharField(max_length=100)
    nascimento = models.DateField()

    def __str__(self):
        return self.nome
    
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE)
    ano_lancamento = models.IntegerField()
    genero = models.CharField(max_length=60)

    def __str__(self):
        return self.titulo

