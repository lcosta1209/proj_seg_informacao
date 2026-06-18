from django.db import models

class Curriculo(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=254)
    site = models.URLField(max_length=500, blank=True)
    experiencia = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} <{self.email}>"