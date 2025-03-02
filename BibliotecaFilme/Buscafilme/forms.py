from django import forms

class BuscarFilmeForm(forms.Form):
    titulo = forms.CharField(
        label="Nome do Filme",
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o nome do filme...'
        })
    )