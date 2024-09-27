from django.contrib import admin
from django.urls import path, include
from projetoteste.views import PaginaInicialViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router_projetoteste = routers.DefaultRouter()
router_projetoteste.register('paginainicial', PaginaInicialViewSet, basename='Pagina Inicial')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router_projetoteste.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
