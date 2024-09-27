from django.contrib import admin
from django.urls import path, include
from projetoteste.views import PaginaInicialViewSet
from rest_framework import routers

router_projetoteste = routers.DefaultRouter()
router_projetoteste.register('paginainicial', PaginaInicialViewSet, basename='Pagina Inicial')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router_projetoteste.urls)),
]
