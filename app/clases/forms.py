from .models import Clase
from django.forms import ModelForm 
from django import forms

class ClaseFormulario(ModelForm):
    class Meta:
        model = Clase
        widgets = {
            'nombre': forms.widgets.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'semestre': forms.widgets.NumberInput(
                attrs={
                    'type' : 'number',
                    'class': 'form-control'
                }
            ),
        }
        fields = ['nombre', 'semestre']