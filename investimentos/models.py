from django.db import models

class TipoAtivo(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Ativo(models.Model):
    ticker = models.CharField(max_length=10, unique=True)
    nome_empresa = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoAtivo, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.ticker} - {self.nome_empresa}"

class Lancamento(models.Model):
    TIPO_OPERACAO = [
        ('C', 'Compra'),
        ('V', 'Venda'),
    ]

    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE)
    data = models.DateField()
    quantidade = models.DecimalField(max_digits=12, decimal_places=4)
    preco_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    taxas = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tipo_operacao = models.CharField(max_length=1, choices=TIPO_OPERACAO)

    @property
    def valor_total(self):
        return (self.quantidade * self.preco_unitario) + self.taxas

    def __str__(self):
        return f"{self.tipo_operacao} {self.quantidade} {self.ativo.ticker} em {self.data}"
