from socket import fromshare
from django import forms

class FormularioPlatos(forms.Form):
    
    PLATOS = (
        (1,'Entrada'),
        (2, 'Plato Fuerte'),
        (3, 'Postre')
    )
        
    nombre = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    descripcion = forms.CharField(
        required=False,
        max_length=200,
        widget=forms.Textarea(attrs={'class':'form-control mb-3'})
    )
    fotografia = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    precio = forms.CharField(
        required=True,
        max_length=200,
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'})
    )
    tipo = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class':'form-control mb-3'}),
        choices=PLATOS
    )