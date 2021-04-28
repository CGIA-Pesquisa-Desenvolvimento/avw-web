from django.db import models


class Ativo(models.Model):
    TIPO_ATIVO = (
        ('A', 'Ação'),
        ('F', 'Fundo Imobiliario'),
    )
    codigo = models.CharField("Código", max_length=12)
    nome_amigavel = models.CharField("Nome", max_length=60)
    tipo_ativo = models.CharField("Tipo de Ativo", max_length=1, choices=TIPO_ATIVO)
    gestor = models.CharField(max_length=60)
    data_ipo = models.DateField("Data da IPO")
    valor_ipo = models.DecimalField("Valor na IPO", max_digits=14, decimal_places=2)
    segmento = models.CharField(max_length=60)
    data_entrada = models.DateField()
    valor_patrimonial_inicial = models.DecimalField("Valor Patrimonial", max_digits=14, decimal_places=2)
    valor_mercado_inicial = models.DecimalField("Valor de Mercado", max_digits=14, decimal_places=2)
    valor_cota_adquirida = models.DecimalField("Valor Cota Adquirida", max_digits=14, decimal_places=2)
    numero_cotas_adquiridas = models.DecimalField("Quantidade de Cotas", max_digits=14, decimal_places=2)
    taxa_b3 = models.DecimalField("Custos B3", max_digits=4, decimal_places=2, blank=True, null=True)
    taxa_liquidacao = models.DecimalField("Taxa Liquidação", max_digits=4, decimal_places=2, blank=True, null=True)
    emolumentos = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    motivo_compra = models.TextField("Motivo da Compra", blank=True, null=True)
    regulamento = models.TextField(blank=True, null=True)
    obs = models.TextField("Observações", blank=True, null=True)

    def __str__(self):
        return self.nome_amigavel
