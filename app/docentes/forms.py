from .models import Docente
from django.forms import ModelForm 
from django import forms

class DocenteFormulario(ModelForm):
    class Meta:
        model = Docente
        widgets = {
            'nombre': forms.widgets.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'apellido': forms.widgets.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
        fields = ['nombre', 'apellido']