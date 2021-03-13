from django import forms


from .models import Pessoa


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields ='__all__'
        # fields = ('nome', 'telefone')
        # exclude = ('celular', 'email')