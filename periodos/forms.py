from .models import Periodo
from django.forms import ModelForm 
from django import forms

class PeriodoFormulario(ModelForm):
    class Meta:
        model =     Periodo
        widgets = {
            'nombre': forms.widgets.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
        fields = ['nombre']