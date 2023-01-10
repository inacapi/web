from .models import Evaluacion
from django.forms import ModelForm 
from django import forms

class EvaluacionFormulario(ModelForm):
    class Meta:
        model = Evaluacion
        widgets = {
            'clase': forms.widgets.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'porcentaje': forms.widgets.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'numero': forms.widgets.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            
        }
        fields = '__all__'