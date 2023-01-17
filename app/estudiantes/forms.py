from .models import Estudiante
from django.forms import ModelForm 
from django import forms

class DocenteFormulario(ModelForm):
    class Meta:
        model = Estudiante
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



class EstudianteFormulario(ModelForm):
    class Meta:
        model = Estudiante
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



