import re
from django import forms
from .models import Curriculo

TELEFONE_RE = re.compile(r'^[0-9 ()+\-]{0,20}$')

class CurriculoForm(forms.ModelForm):
    class Meta:
        model = Curriculo
        fields = ['nome', 'telefone', 'email', 'site', 'experiencia']
        widgets = {
            'nome': forms.TextInput(attrs={'maxlength': 200}),
            'telefone': forms.TextInput(attrs={'maxlength': 20, 'placeholder': '(00) 00000-0000'}),
            'email': forms.EmailInput(attrs={'maxlength': 254}),
            'site': forms.URLInput(attrs={'maxlength': 500, 'placeholder': 'https://...'}),
            'experiencia': forms.Textarea(attrs={'rows': 8, 'maxlength': 5000}),
        }
        error_messages = {
            'nome': {'required': 'Nome é obrigatório.'},
            'email': {
                'required': 'E-mail é obrigatório.',
                'invalid': 'E-mail informado não é válido.',
            },
            'experiencia': {'required': 'Experiência profissional é obrigatória.'},
            'site': {'invalid': 'Endereço web deve começar com http:// ou https://'},
        }

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone', '').strip()
        if telefone and not TELEFONE_RE.match(telefone):
            raise forms.ValidationError(
                "Telefone deve conter apenas números, espaços, '+', '-', '(' e ')'."
            )
        return telefone