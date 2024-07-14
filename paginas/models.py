from django.db import models

# Create your models here.
class Categoria(models.Model):
    data = models.DateField(auto_now_add=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
class Fotografia(models.Model):
    data = models.DateField(auto_now_add=True)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)
    foto = models.CharField(max_length=250)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)

    def __str__(self):
        return self.nome