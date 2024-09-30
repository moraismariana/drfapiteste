from projetoteste.models import PaginaInicial
from projetoteste.serializers import PaginaInicialSerializer
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PermissaoProjetoTeste(permissions.BasePermission):
    """
    Permissão personalizada para verificar se o usuário faz parte do grupo de editores.
    """
    def has_permission(self, request, view):
        # Permite acesso de leitura para qualquer usuário
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Verifica se o usuário está no grupo 'Editores Projeto Teste'
        return request.user.groups.filter(name='Editores Projeto Teste').exists()

class PaginaInicialViewSet(viewsets.ModelViewSet):
    queryset = PaginaInicial.objects.all()
    serializer_class = PaginaInicialSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoProjetoTeste]