from dataclasses import field
from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
    class Meta:
        model = Prueba
        fields = ('titulo', 'subtitulo', 'cantidad')
        #fields = ('__all__')
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese texto aqui'
                }
            )
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('El numero ingresado debe ser mayor a 10')
        return cantidad