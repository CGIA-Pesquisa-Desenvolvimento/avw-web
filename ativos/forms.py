from django import forms

from .models import Ativo


class AtivoModelForm(forms.ModelForm):

    class Meta:
        model = Ativo
        fields = ('nome_amigavel', 'gestor', 'segmento', 'numero_cotas_adquiridas')
