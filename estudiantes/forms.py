from .models import Estudiantes
from django.forms import ModelForm 
from django import forms

class EstudiantesFormulario(ModelForm):
    class Meta:
        model = Estudiantes
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