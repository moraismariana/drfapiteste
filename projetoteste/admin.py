from django.contrib import admin
from projetoteste.models import PaginaInicial

class PaginaInicialAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

admin.site.register(PaginaInicial, PaginaInicialAdmin)