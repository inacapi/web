from .models import Estudiante, Matricula
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


class MatriculaFormulario(ModelForm):
    class Meta:
        model = Matricula
        widgets = {

            'id': forms.widgets.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),


            'periodo': forms.widgets.Select(
                attrs={
                    'class': 'form-select'
                }
            ),


        }
        fields = ['id', 'periodo']
