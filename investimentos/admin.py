from django.contrib import admin
from .models import Instituicao, Conta, TipoAtivo, Ativo, Lancamento, MovimentacaoConta

@admin.register(Instituicao)
class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Conta)
class ContaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instituicao', 'tipo', 'saldo_inicial')
    search_fields = ('nome', 'instituicao')

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
    list_display = ('data', 'conta', 'ativo', 'tipo_operacao', 'quantidade', 'preco_unitario', 'valor_total')
    list_filter = ('tipo_operacao', 'ativo', 'data')
    date_hierarchy = 'data'

@admin.register(MovimentacaoConta)
class MovimentacaoConta(admin.ModelAdmin):
    list_display = ('data', 'conta', 'valor', 'descricao', 'tipo')
    list_filter = ('conta', 'data')
    date_hierarchy = 'data'
