from projetoteste.models import PaginaInicial
from projetoteste.serializers import PaginaInicialSerializer
from rest_framework import viewsets

class PaginaInicialViewSet(viewsets.ModelViewSet):
    queryset = PaginaInicial.objects.all()
    serializer_class = PaginaInicialSerializer