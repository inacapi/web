from .models import Nota
from django.forms import ModelForm 
from django import forms

class NotaFormulario(ModelForm):
    class Meta:
        model = Nota
        widgets = {
            'inscripcion': forms.widgets.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'evaluacion': forms.widgets.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'nota': forms.widgets.NumberInput(
                attrs={
                'class': 'form-control'
                }
            )
            
        }
        fields = '__all__'