from .models import Seccion
from django.forms import ModelForm 
from django import forms

class SeccionFormulario(ModelForm):
    class Meta:
        model = Seccion
        widgets = {

            'id' : forms.widgets.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'docente': forms.widgets.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'clase': forms.widgets.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'periodo': forms.widgets.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
        }
        fields = '__all__' 