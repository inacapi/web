from .models import Inscripcion
from django.forms import ModelForm 
from django import forms

class IncripcionFormulario(ModelForm):
    class Meta:
        model = Inscripcion
        widgets = {
            'matricula': forms.widgets.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'periodo': forms.widgets.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'seccion': forms.widgets.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            
        }
        fields = '__all__'