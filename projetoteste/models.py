from django.db import models

class PaginaInicial(models.Model):
    secao1_titulo = models.CharField(max_length=150)
    secao1_texto = models.TextField()

    secao2_titulo = models.CharField(max_length=150)
    secao2_texto = models.TextField()

    secao3_titulo = models.CharField(max_length=150)
    secao3_texto = models.TextField()