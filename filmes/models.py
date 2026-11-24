from django.db import models

# Create your models here.

class Diretor(models.Model):
    nome = models.CharField(max_length=120)

    class Meta:
        ordering = ["nome"]
        verbose_name_plural = "Diretores"

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=80)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    ano_lancamento = models.PositiveIntegerField(null=True, blank=True)
    diretor = models.ForeignKey(
        Diretor,
        on_delete=models.CASCADE,
        related_name="filmes",
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="filmes",
    )

    class Meta:
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo