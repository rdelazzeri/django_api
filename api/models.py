from django.db import models

class Livro(models.Model):
    codigo = models.CharField(max_length=30, null=True, blank=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    ano_publicacao = models.CharField(max_length=4)
    data_cadastro = models.DateField()
    numero_paginas = models.IntegerField()
    preco = models.DecimalField(max_digits=18, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.autor} - {self.titulo}'


