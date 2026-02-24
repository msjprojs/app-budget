from django.contrib import admin
from .models import TipoAtivo, Ativo, Lancamento

@admin.register(TipoAtivo)
class TipoAtivoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Ativo)
class AtivoAdmin(admin.ModelAdmin):
    list_display = ('ticker', 'nome_empresa', 'tipo')
    search_fields = ('ticker', 'nome_empresa')

@admin.register(Lancamento)
class LancamentoAdmin(admin.ModelAdmin):
    list_display = ('data', 'ativo', 'tipo_operacao', 'quantidade', 'preco_unitario', 'valor_total')
    list_filter = ('tipo_operacao', 'ativo', 'data')
    date_hierarchy = 'data'
